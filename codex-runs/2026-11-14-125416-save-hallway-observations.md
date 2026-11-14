# Save the hallway trace observations in the run archive

- Objective — Preserve the previous hallway trace diagnosis in an outputs Markdown file.
- Changes — Added outputs/memory-hallway-all-48-20261114-123128/report/hallway-trace-observations.md with the branch outcomes, turn loop, missing cue recall and links to supporting traces. Updated that run's report/artifact-index.json to include the new note. Added this Codex record. These changes are in the working tree on embodiedmind-experiment, with original hallway evidence in ca70ef2.
- Rationale — Placed the note alongside the episode metrics and report so its references resolve within the archive. Updated the hallway archive index directly so existing run evidence stayed intact. The earlier combined report index remains a snapshot of its original bundle.
- Verification — Hashed each indexed file using WSL Python and verified all 1,436 hallway archive entries. No experiment or external change.
