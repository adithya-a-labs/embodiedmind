"""Serve the browser viewer and its local JSON endpoints."""

import json
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

from embodiedmind.agents import VARIANTS
from embodiedmind.reasoning.llm_client import InferenceUnavailable
from embodiedmind.environments.dynamic_world import DYNAMIC_ENV_ID, INTERVENTIONS
from embodiedmind.environments.factory import OFFICIAL_ENVIRONMENTS
from embodiedmind.viewer.data import ViewerData


ASSETS = {
    "/": ("index.html", "text/html"),
    "/viewer.css": ("viewer.css", "text/css"),
    "/viewer.js": ("viewer.js", "text/javascript"),
}


def viewer_origins(port, tunnel_origin=None):
    local = {f"localhost:{port}", f"127.0.0.1:{port}"}
    origins = {f"http://{host}": {host} for host in local}
    if tunnel_origin:
        match = re.fullmatch(r"https://([a-z0-9-]+(?:\.[a-z0-9-]+)*\.devtunnels\.ms)/?", tunnel_origin)
        if not match:
            raise ValueError("Use the exact HTTPS address of your private devtunnels.ms port.")
        host = match[1]
        # A relay can preserve the public Host or rewrite it to the local listener.
        origins[f"https://{host}"] = local | {host}
    return origins


def serve(runs, sandbox_output, models, port, tunnel_origin=None, workflows=None):
    viewer_origins(port, tunnel_origin)
    data = ViewerData(runs, sandbox_output, models, workflows)
    assets = Path(__file__).with_name("static")

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *_):
            pass

        def send(self, status, content_type, content):
            self.send_response(status)
            self.send_header("Content-Type", content_type + "; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Content-Security-Policy",
                             "default-src 'self'; frame-ancestors 'none'; object-src 'none'")
            self.end_headers()
            try:
                self.wfile.write(content)
            except (BrokenPipeError, ConnectionResetError):
                pass

        def payload(self, status, value):
            self.send(status, "application/json", json.dumps(value).encode("utf-8"))

        def dispatch(self, method):
            if self.headers.get("Host") not in accepted_hosts:
                self.payload(403, {"error": "Use the local viewer address."})
                return
            parsed = urlsplit(self.path)
            params = parse_qs(parsed.query)
            try:
                if method == "POST" and parsed.path == "/api/sandbox":
                    origin = self.headers.get("Origin")
                    if self.headers["Host"] not in origins.get(origin, set()):
                        self.payload(403, {"error": "Open Sandbox from an approved viewer address."})
                        return
                    if self.headers.get_content_type() != "application/json":
                        raise ValueError("Expected JSON sandbox controls.")
                    length = int(self.headers.get("Content-Length", 0))
                    if not 0 < length <= 2 * 1024 * 1024:
                        raise ValueError("Invalid sandbox request size.")
                    value = data.sandbox(json.loads(self.rfile.read(length)))
                elif method == "GET" and parsed.path in ASSETS:
                    asset, content_type = ASSETS[parsed.path]
                    self.send(200, content_type, (assets / asset).read_bytes())
                    return
                elif method == "GET" and parsed.path == "/favicon.ico":
                    self.send(204, "image/x-icon", b"")
                    return
                elif method == "GET" and parsed.path == "/api/catalog":
                    value = {"runs": data.catalog(include_coverage=params.get("coverage") == ["1"]),
                             "environments": [*OFFICIAL_ENVIRONMENTS, DYNAMIC_ENV_ID],
                             "variants": list(VARIANTS), "interventions": INTERVENTIONS}
                elif method == "GET" and parsed.path == "/api/jobs":
                    value = data.jobs(params["run"][0])
                elif method == "GET" and parsed.path == "/api/replay":
                    value = data.replay(params["run"][0], params["job"][0])
                elif method == "GET" and parsed.path == "/api/live":
                    value = data.live(params["run"][0])
                else:
                    self.payload(404, {"error": "Viewer page unavailable."})
                    return
                self.payload(200, value)
            except FileNotFoundError as exc:
                self.payload(404, {"error": str(exc)})
            except (TypeError, KeyError, ValueError) as exc:
                self.payload(400, {"error": str(exc)})
            except InferenceUnavailable as exc:
                self.payload(503, {"error": str(exc)})

        def do_GET(self):
            self.dispatch("GET")

        def do_POST(self):
            self.dispatch("POST")

    with ThreadingHTTPServer(("127.0.0.1", port), Handler) as server:
        origins = viewer_origins(server.server_port, tunnel_origin)
        accepted_hosts = set().union(*origins.values())
        print(f"EmbodiedMind viewer: http://127.0.0.1:{server.server_port}", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
