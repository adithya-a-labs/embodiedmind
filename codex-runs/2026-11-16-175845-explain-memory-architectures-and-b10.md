# Explain EmbodiedMind architectures and B10 performance

- Objective — Explain the original research question, B0–B10 and controls, and the evidence behind B10's gains and remaining failures.
- Sources — Read the Notion proposal, architecture guide and retrospective. Checked the current agent registry, B2/B3 memory, B9/B10 task state, action arbitration, mission controller, runner and ledger. Cross-checked the original held-out results, B9 audit and matched B9/B10 report.
- Verification — Parsed saved manifests, summaries and JSONL traces for matched DoorKey and Blocked Unlock Pickup seed 4002 and GoToShift relocation seed 4003. Confirmed action sequences, model goals, executed decisions and outcomes. A Windows ripgrep glob was invalid. Used directory-wide searches and exact paths. No simulator or inference ran.
- Decisions — Framed B10 as a controller and memory bundle evaluated on layouts used for diagnosis. Separated the 48-action comparison from MultiRoom at 80 and reported the relocation regression. The user asked for explanation, so the Notion pages were used as sources.
- Changes — Added this local Markdown record on embodiedmind-experiment at 1480182d. Existing viewer edits and other run notes belong to separate work. No source files, Git refs or Notion pages changed in this run.
