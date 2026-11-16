# Fix stale replay selections when switching runs

- Objective — Diagnose the reported tunnel replay failure. The screenshot paired a MultiRoom archive with a GoToObjMaze scenario and showed Unknown episode.
- Changes — Updated src/embodiedmind/viewer/static/viewer.js to clear and disable episode controls during run changes, bind episode requests to the loaded run, and ignore superseded responses. Added this record. No tunnel settings or experiment data changed. Changes remain in the working tree on embodiedmind-experiment, last verified at 1480182d.
- Verification — Node syntax and a delayed-response regression check passed. The running viewer served the updated script, listed all 20 MultiRoom jobs, and returned HTTP 200 for a replay using the tunnel Host header. Signed-in phone access remains unverified.
