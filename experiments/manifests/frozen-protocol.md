# EmbodiedMind experiment registration

Freeze recorded before held-out outcomes. The Git commit containing this file and the exact hashes recorded in the run manifests bind the code, model configuration, roster, software lock, runtime, and report. Resume from that commit and retain previous attempts.

## Design and rosters

- Development: seeds 0–4 for each stock benchmark environment and B0–B3. Separate smoke fixture 42. Custom development: 0 and 1 across B1–B3 and all intervention assignments.
- Static held-out: 1000–1029 in each of the two stock environments, B0–B3, 240 episodes, one realized replicate per cell.
- Dynamic held-out: 2000–2029 for the custom GoToShift task, B1–B3 crossed with no change, dropout and relocation, 270 episodes. Initial layout and task are paired across conditions. All arms use two identical scripted left turns after the initial view, with no model decision during this prefix. This makes both target positions hidden at the fixed intervention trigger after step 2. Masking continues through step 9 at probability 0.25. Reserve the carrying and immediate forward cells.
- Relocation attempts exactly once, and moves the target only when both cells are hidden, the destination is free and a valid goal remains reachable. Preserve all valid assigned episodes, including missed exposure. Main dynamic comparison is intention-to-treat. Report applied/missed exposure by variant and reason. Exposed-only results are descriptive.

## Common controls

All variants see the same public symbolic observation adapter, route hints based only on the current view, action vocabulary, primitive executor, generation options and budgets within each comparison. The same frozen Qwen model and quantization are used throughout. There are 36 decisions/steps per static episode and 24 per dynamic episode, one model call per model decision (the two scripted dynamic turns count against steps), a common 768-byte ASCII memory ceiling and common output/context caps. B0 has an empty memory payload. B3 aging is 12 steps. Model seeds are paired by episode seed and decision index. One inference slot is frozen after development calibration. No world rendering, privileged coordinates, score, hidden state or evaluated outcomes enter agent inputs. Steps, seeds and variants are interleaved as specified in the versioned roster generator.

## Outcomes and missing data

Static primary endpoint is B3 minus B1 mission success by environment. Dynamic primary endpoint is B3 minus B2 explicitly cited contradicted evidence actions per executed step, by assigned intervention. Keep success and all secondary outcomes, including steps, inference calls, token use, latency, invalid actions, unsupported evidence references, and time to task success after an observed contradiction. A stale action is observable here when the emitted evidence citation refers to an invalidated fact. Unsupported evidence cites a missing or invalid source identifier. These outcomes measure citations, with incomplete visibility into uncited model behavior. H3 is descriptive across the dynamic arms. The B3 versus B2 comparison bundles revision, age warnings and working memory.

Use identical seed, environment, mission, intervention and replicate for paired comparisons. Use seed-paired bootstrap intervals when there are at least five matched seeds. Valid task failures, budget timeouts, negative and null effects stay in the analysis. Record every infrastructure attempt; retry a transient inference failure up to twice with bounded backoff, using the same job ID and fresh attempt ID. A corrupt artifact, unmatched pair, or invariant violation blocks acceptance until recovered. Intervention no-ops never qualify for removal. If held-out inspection inspires a methodological change, version the design and register fresh disjoint data before a revised comparison.

## Evidence

Store complete agent-visible observations, prompts, outputs, actions, inference telemetry and evaluator-only events in immutable hashed episode folders. Save representative headless frames and replays. Audit roster coverage and regenerate all figures and the technical report from finalized raw traces.
