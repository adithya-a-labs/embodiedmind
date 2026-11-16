# Inspect B4 and B5 relocation trajectories

- Objective — Compare actual post-relocation decisions and explain seed 5 and the agentic distinction.
- Evidence — Read all ten B4/B5 episode trajectories in outputs/memory-relocation-all-20261114-121139, seed 5 evaluator records, and grounding.py. Used zero-based trace steps. On seed 5 the old sighting was contradicted at step 4. The exploration route went south and east while the new key was northwest and never entered the policy-visible candidates. This describes the recorded route, and no counterfactual search was tested.
- Verification — Compared first post-relocation sightings, ruled-out cells, goal choices, executed actions, routes, and evaluator coordinates. Confirmed the shared guard and B5-only goal interface from the controller mode flags.
- Changes — Created this working-tree record on embodiedmind-experiment. Evidence commit 6f56667. No code, experiment evidence or external record changed.
