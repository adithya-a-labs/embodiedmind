# Compare the viewer through localhost and the private tunnel

- Objective — Diagnose why the private tunnel view appears broken while localhost works.
- Verification — From Windows, the homepage, CSS, JavaScript, and catalog returned HTTP 200 with their expected content types. Each corresponding unauthenticated tunnel request returned HTTP 302. Checked the viewer's same-origin asset and API paths and Microsoft Dev Tunnels access documentation.
- Result — The phone's signed-in failure could not be reproduced from the unauthenticated check. A screenshot or error from the phone is needed to distinguish a layout issue from a failed asset or API request. Last verified branch embodiedmind-experiment at 1480182d. Added this local run record. No source or service settings changed.
