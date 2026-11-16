# Forward the viewer through a new private Dev Tunnel

- Objective — Provide a new private phone-access link for the EmbodiedMind viewer on port 8765.
- Changes — Opened a local Windows VS Code window and forwarded port 8765. VS Code showed rnr10zrb-8765.inc1.devtunnels.ms as Private. Restarted only the WSL viewer with that exact tunnel origin. Added this local run record. No project source changed. Last verified branch embodiedmind-experiment at 1480182d.
- Verification — Windows localhost responded before forwarding. A PowerShell quoting error prevented the first restart command from running. Retried via a WSL Bash script with a process working-directory check. The viewer catalog returned HTTP 200 for the new Host header and the private relay returned HTTP 302 without authentication. Signed-in phone access remains unverified. No experiment ran.
