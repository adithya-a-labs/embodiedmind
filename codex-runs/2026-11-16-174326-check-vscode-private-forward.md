# Check the VS Code private port forward

- Objective — Check port 8765 and reconnect the existing private tunnel for phone access.
- Findings — The WSL VS Code Ports panel shows 8765 auto-forwarded to 127.0.0.1:8765. Windows localhost returned HTTP 200. The local VS Code Ports panel shows no forwarded ports. The saved VS Code port-forwarding state does not contain the requested tunnel ID.
- Outcome — Could not reconnect the exact private tunnel from the current VS Code state. No replacement tunnel or access change was made. The local viewer remains available. Added this run record in the EmbodiedMind workspace, last verified at 1480182d. No experiment ran.
