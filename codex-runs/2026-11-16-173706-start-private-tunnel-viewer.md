# Start the private-tunnel viewer

- Objective — Start the EmbodiedMind dashboard on port 8765 and check the existing private Dev Tunnel.
- Changes — Started a detached WSL viewer with the existing tunnel origin. Added this uncommitted record. No source or tunnel settings changed.
- Verification — On embodiedmind-experiment at 1480182d, checked the listening socket, received HTTP 200 from the viewer with the tunnel Host header and from Windows localhost, and received HTTP 302 from the private HTTPS tunnel to the Microsoft tunnel service. An authenticated phone session was unavailable for the end-to-end check. No experiment ran.
