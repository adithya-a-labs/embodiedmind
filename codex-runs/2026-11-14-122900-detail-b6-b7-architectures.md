# Expand the B6 and B7 memory architecture reference

- Objective — Add detailed B6 and B7 architecture walkthroughs to the open Notion reference. The variants already exist in the repository, so interpreted this as documenting the implementations.
- External change — Replaced the short B6/B7 subsection of https://app.notion.com/p/418f975653bf818f85effad4cbef3839 with dedicated sections covering extraction, phase selection, prompt retrieval, cue texts, controls and actual DoorKey decisions. Preserved the surrounding reference.
- Verification — Read workflow and controller code, scheduler controls and saved DoorKey trajectories for both variants on seeds 5 through 9. At seed 5, both matched through step 7 and diverged at the door on step 8. Read back the updated Notion page to check the new sections and surrounding content.
- Repository — Branch embodiedmind-experiment. This Codex record is the only new working-tree file. No source changes or new experiment runs. Evidence is in outputs/memory-doorkey-v2-dev-20261114.
