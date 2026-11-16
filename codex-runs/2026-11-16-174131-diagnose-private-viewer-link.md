# Diagnose private viewer link access

- Objective — Determine why the existing private Dev Tunnel link does not open the viewer.
- Result — The viewer returned HTTP 200 from Windows localhost on port 8765. Following the private tunnel redirect returned the GitHub sign-in page. An authorized browser session is needed to verify forwarding beyond the authentication gate.
- Verification — Used curl against the local port and private URL and inspected the final HTML title. The first redirect probe did not finish and a subsequent probe succeeded. Last verified repo revision was 1480182d on embodiedmind-experiment. Added this local run record. No tunnel or source settings changed.
