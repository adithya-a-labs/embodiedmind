<!-- Source: https://app.notion.com/p/417f975653bf81afa292d347c362b39d | snapshot 2026-11-14 IST | v1.0 with full-study amendment -->

## LIVE PROGRESS SNAPSHOT — 14 November 2026 (04:02 IST conversation checkpoint)

<b>Status:</b> Infrastructure bootstrap completed as reported by user; <b>first autonomous LLM-controlled BabyAI episode has NOT been confirmed</b>. This section supersedes older “not yet implemented” infrastructure status language, but does not change the scientific hypotheses or protocol.

<b>Evidence classification:</b> The following setup items are user-reported. Ollama model ID, GPU percentage and context size are supported by the actual pasted terminal output. I have not inspected the local WSL filesystem, executed any of these commands, or verified the Git repository.

| Workstream | Status | Evidence / qualification |
| --- | --- | --- |
| Windows host + WSL2 | Reported working | Windows 11; Ubuntu 22.04.5 LTS; WSL username \`adithyaa\` |
| Native Linux workspace | Reported working | \`/home/adithyaa/Projects/EmbodiedMind\`; \`.venv/\` active |
| Python setup | Reported working | \`uv\` managed Python 3.12.16 in project; Ubuntu system Python 3.10.12 retained for ROS 2 Humble |
| NVIDIA hardware | Reported detected | GeForce RTX 5070 Ti, 12 GB VRAM |
| MiniGrid / BabyAI | Smoke-test reported completed | Environment initial smoke test passed; actual version, exact test env, seeds and logs not supplied |
| Ollama | Reported service active | v0.40.16, WSL loopback \`127.0.0.1:11434\` |
| Qwen 2.5 3B | <b>Confirmed in pasted terminal output</b> | \`qwen2.5:3b-instruct\`; ID \`357c53fb659c\`; loaded size 2.2 GB; \`100% GPU\`; 4096 context; \`llamacpp\` runner; produced \`READY\` |
| Ollama local JSON API | User-confirmed complete | User replied “done” after proposed API JSON test; precise returned JSON and request log were not shared |
| PyTorch CUDA | <b>Not verified</b> | Installation and CUDA matmul test pending confirmation |
| Stable-Baselines3 / SB3-Contrib / TensorBoard | <b>Not verified</b> | Suggested for later RL extensions, NOT blocking frozen-LLM memory study |
| Docker, GitHub remote and Codex CLI | <b>Not verified</b> | Existence/authentication/connectivity not yet established |
| First BabyAI LLM episode | <b>Not verified / next milestone</b> | A \`first\_llm\_[episode.py](http://episode.py)\` example and run instructions were provided in chat, but there is no output proving the file was saved or the episode executed |

<b>Model output evidence (from pasted terminal):</b> \`NAME qwen2.5:3b-instruct \| ID 357c53fb659c \| SIZE 2.2 GB \| PROCESSOR 100% GPU \| CONTEXT 4096 \| RUNNER llamacpp\`. The model generated \`READY\` after download. This proves successful inference, not successful environment planning.

<b>Core research architecture remains four variants</b>: B0 reactive; B1 bounded text history; B2 structured episodic/spatial memory without contradiction revision; B3 full hybrid evidence-and-belief revision. A separate machine setup summary listed only three; retain B2 so the research can isolate the effect of explicit revision.

<b>Immediate next milestone:</b> Verify and commit the Phase 0 scaffold, then pass the observation/action and evaluator-isolation checks before running one seeded GoToObj development smoke episode. Save the complete JSONL trace. Use the result to verify orchestration before building out B1/B2/B3.

<b>Resume environment (WSL):</b>

```bash
cd ~/Projects/EmbodiedMind
source .venv/bin/activate
python --version
ollama list
ollama ps
```

<b>Pilot handoff:</b> Check whether \`first\_llm\_[episode.py](http://episode.py)\` exists before creating or modifying it. Inspect its observation coordinate convention and reward/termination logic; run \`python first\_llm\_[episode.py](http://episode.py)\` if present and appropriate. Capture seed, environment ID, model name and digest, observation text, actions, rewards, errors, token use (if available) and a run manifest. A successful single episode is a smoke-test result, not evidence that B3 outperforms B1.

<b>Priority constraint:</b> The CaCTüS application deadline is <date start="2026-11-16" />. Do not delay the application to finish research extensions.

---

<callout icon="🧭" color="gray_bg">
Execution companion: <mention url="https://app.notion.com/p/417f975653bf81e3a17ee53d1430006e">EmbodiedMind — Agent Roadmap & Research Execution Guide (v1.0)</mention>. The companion is the operational checklist, gate tracker, recovery protocol and recurring agent self-audit; the proposal on this page is the scientific source of truth.
</callout>

<callout icon="🔬" color="blue_bg">
RESEARCH DESIGN • v1.0 • Created <date start="2026-11-14" /> • Status: RESEARCH DESIGN COMPLETE; INFRASTRUCTURE BOOTSTRAPPED; FIRST LLM-CONTROLLED EPISODE NOT YET VERIFIED. See live progress snapshot above. This is an independent pilot inspired by the 2027 CaCTüS project descriptions; it is not an official Max Planck research project, lab affiliation, or validated result.
</callout>

<b>Canonical context:</b> <mention url="https://app.notion.com/p/3f6f975653bf812aa570e32057608b70">Max Planck Tübingen — CaCTüS</mention>. The application deadline in the opportunity record is <date start="2026-11-16" />. The CaCTüS project-description PDF provided by the applicant is the basis for the project-number mappings below. See companion execution runbook linked from this page.

<table-of-contents />

## A. Project identity and executive abstract

<b>Working title:</b> EmbodiedMind: Evaluating Evidence-Grounded Memory and Belief Revision in LLM-Based Embodied Agents

<b>One-sentence proposition:</b> Test whether an LLM-driven agent navigating a partially observable, language-instructed world completes tasks more reliably when it maintains evidence-grounded episodic/spatial memory and explicitly revises stale beliefs, compared with agents using only current observations or unstructured text history.

<b>Abstract.</b> Autonomous language-model agents often act on incomplete sensory information and must combine past observations with newly acquired evidence. We propose a controlled benchmark in MiniGrid/BabyAI in which a frozen local LLM selects high-level actions for an embodied, discrete-action agent. Identical language missions and partially observed environments are evaluated across four memory conditions: reactive, unstructured text-history, structured spatial/episodic memory, and structured memory with evidence-based belief revision. Standard static environments establish basic capabilities; an explicitly labeled extension introduces sensor corruption and reachable, out-of-view world changes to expose stale beliefs. Paired-seed experiments measure mission completion, action and inference costs, stale-knowledge failures, belief consistency, and recovery after contradiction. The goal is not to claim a novel foundation model or real-robot transfer, but to identify mechanisms and failure modes that help explain when explicit memory aids language-conditioned embodied decision-making.

<b>Research classification:</b> Embodied decision-making; agentic LLMs; agent memory; partial observability; language-conditioned navigation; uncertainty-aware planning.

<b>Boundary of claim:</b> MiniGrid is an abstract 2D environment with discrete actions and no realistic rigid-body dynamics. The work concerns cognitive/planning aspects relevant to Physical AI, NOT proof of physical robot manipulation, sensor calibration, grasping, or sim-to-real performance.

## B. Motivation and why the question matters

A physically situated agent cannot reliably answer “where is the blue key?” from a single local observation if it saw the key several steps earlier. But naive memory has a second failure mode: once an object moves, remembering its old location can actively mislead the agent. Language models are powerful task interpreters but can generate confident descriptions of information never directly observed or no longer current. The research seeks to separate three capacities: (1) preserving relevant evidence, (2) constructing a usable partial world model, and (3) revising that model when observations contradict previous beliefs.

The motivating use case is not a chatbot with a long prompt: it is an action-taking system in which incorrect beliefs have measurable consequences (extra movement, unsuccessful manipulation, timeouts, and invalid action attempts).

## C. Research questions, hypotheses and falsification

<b>RQ1 (memory utility).</b> Do evidence-grounded structured memories improve task success or action efficiency over equal-budget natural-language history on held-out partially observable missions?

<b>RQ2 (staleness and revision).</b> When facts change, do explicit provenance and contradiction-handling reduce actions aimed at outdated object positions?

<b>RQ3 (information acquisition).</b> Does uncertainty-aware memory change when an agent chooses to explore, re-observe or verify information rather than immediately act?

<b>RQ4 (trade-offs).</b> What are the added LLM-token, inference-time and implementation costs, and in which conditions does structured memory cause more harm than benefit?

Hypotheses to preregister, not assert as facts:

- <b>H1:</b> On held-out multi-room missions, the full hybrid-memory agent will have higher task-completion rate than the bounded-text-history agent.
- <b>H2:</b> Under hidden object relocation / contradictory observations, hybrid memory with revision will produce fewer stale-location actions than structured memory without revision.
- <b>H3:</b> Any memory benefit will increase with observation delay or controlled missing information.
- <b>H4:</b> Hybrid memory may incur greater processing cost and may fail when its odometry, entity association or update rules are wrong.

<b>Null possibilities:</b> Natural-language history may match or outperform structured memory; explicit revision may offer no benefit; extra structure may introduce brittle assumptions. Report these faithfully.

## D. Relationship to CaCTüS 2027 topics

The official applicant-supplied project list includes:

| CaCTüS number | Official topic | Connection (conceptual, not claimed collaboration) |
| --- | --- | --- |
| 3 | Integration and Verbalization of Novel Abilities in Language Models | Skill generalization and LLM behavior; we do NOT fine-tune models in the core experiment |
| 6 | Schema Learning in Deep Meta-Reinforcement Learning for One-Shot Spatial Navigation | Structured knowledge and rapid adaptation; our initial study does NOT reproduce meta-RL or hippocampal remapping |
| 7 | Beyond reward maximization: Embodied agents driven by internal states | Embodied constraints; internal drives and energy budgets are optional future extensions |
| 8 | A library for BAMDP, POMDP and IPOMDP | Explicit partial observability, evidence updates and belief-aware planning; we do NOT claim to implement a full exact POMDP solver |
| 2 | Data-efficient Social Behaviour Analysis | Possible future social-perception extension, outside v1 scope |

These are interpretations of relevance based on project descriptions, not statements by the labs endorsing this architecture. The exact 2027 supervisor of each proposed topic should not be inferred from adjacent papers.

## E. Related literature and verified researcher connections

<b>Direct experimental / theoretical foundations</b>

1. Chevalier-Boisvert et al., <i>BabyAI: A Platform to Study the Sample Efficiency of Grounded Language Learning</i> (2018). Grounded language missions, partially observed agent tasks and sample-efficiency benchmark. [Paper](https://arxiv.org/abs/1810.08272).
2. Chevalier-Boisvert et al., <i>MiniGrid & MiniWorld: Modular & Customizable Reinforcement Learning Environments for Goal-Oriented Tasks</i> (2023). Lightweight, controllable environment foundation. [Paper](https://arxiv.org/abs/2306.13831); [current MiniGrid documentation](https://minigrid.farama.org/).
3. Yao et al., <i>ReAct: Synergizing Reasoning and Acting in Language Models</i> (ICLR 2023). Interleaving decisions, tool actions and environmental feedback; not a memory-comparison benchmark. [Paper](https://arxiv.org/abs/2210.03629).
4. Wang et al., <i>Voyager: An Open-Ended Embodied Agent with Large Language Models</i> (2023). Embodied LLM agent, persistent skill library and experience-driven exploration in Minecraft; an adjacent memory concept, not identical to our belief tracker. [Paper](https://arxiv.org/abs/2305.16291).
5. Ahn et al., <i>Do As I Can, Not As I Say: Grounding Language in Robotic Affordances</i> (2022). Why LLM high-level plans need embodied action grounding. [Paper](https://arxiv.org/abs/2204.01691).

<b>Max Planck / Tübingen research connections</b>

6. Sancaktar, Gumbsch, Zadaianchuk, Kolev & <b>Georg Martius</b>, <i>SENSEI: Semantic Exploration Guided by Foundation Models to Learn Versatile World Models</i> (ICML 2025). VLM-informed exploration with model-based RL; related to semantic exploration, but method differs substantially. [Peer-reviewed paper](https://proceedings.mlr.press/v267/sancaktar25a.html); [Martius’s MPI-IS research profile](https://is.mpg.de/al/person/gmartius). Note: the MPI Autonomous Learning group’s historic configuration has changed; do not describe this paper as a 2027 CaCTüS supervision commitment.
7. Wenting Wang, Tobias Kaufmann & <b>Peter Dayan</b>, <i>Decomposing Response Inhibition: A POMDP Model</i> (PLOS Computational Biology, 2026). Formal belief-state inference under partial observability and associated decision costs in a cognitive experiment, not robotic navigation. [Published paper](https://doi.org/10.1371/journal.pcbi.1014068).
8. <b>Jonas Geiping</b>, Safety- and Efficiency-aligned Learning (SEAL), MPI-IS/ELLIS co-affiliated group, is explicitly named with DMO for the 2027 CaCTüS Project 3 and 4. Relevant background on iterative computation: Geiping et al., <i>Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach</i> (2025). [Paper](https://arxiv.org/abs/2502.05171); [MPI profile](https://is.mpg.de/seal/person/jgeiping). This is NOT an embodied-memory paper.
9. <b>Antonio Orvieto</b>, Deep Models and Optimization (DMO), MPI-IS/ELLIS, co-named for Projects 3 and 4. His research concerns optimization and architectures. [MPI profile](https://is.mpg.de/dmo/person/aorvieto). This is a research-context connection, not a citation claiming he developed our method.

<b>Research integrity:</b> Do not claim originality until reviewing additional embodied-memory, mapping, and language-agent literature. Cite adjacent work for actual contributions rather than projecting this proposal onto it.

## F. Environment specification

<b>World family:</b> Farama MiniGrid + BabyAI via Gymnasium; launch initially in Ubuntu/WSL2 on the RTX 5070 Ti Windows laptop if native Windows dependency behavior is problematic. Pin Python and package versions after smoke test, then record them in a lock/requirements file.

<b>Verified built-in environments to use:</b>

- BabyAI-GoToObjS6-v1: minimal language goal; no doors and no distractors; useful solely for action/observation interface debugging.
- MiniGrid-DoorKey-8x8-v0: key pickup → door unlock → goal; multi-step control.
- BabyAI-GoToObjMazeS7-v0: find a target in a maze with distractors, with partially observed rooms.

<b>Native observation contract:</b> The agent receives the permitted MiniGrid observation dictionary: a 7 × 7 × 3 egocentric symbolic grid encoding, direction, and natural-language mission. The orientation and current carrying state may be obtained from permitted observations or the agent's own action history, but NOT by reading hidden environment state. The simulator's full grid / agent internals may be accessed ONLY by the separate evaluator for ground-truth scoring and replay.

<b>Default primitive action space:</b> 0=left, 1=right, 2=forward, 3=pickup, 4=drop, 5=toggle, 6=done. Not every environment uses every action. The command validator rejects malformed or unsupported requests.

<b>Perception choice for v1:</b> A deterministic adapter decodes the legitimate 7 × 7 symbolic observation into compact, factual text for the LLM (e.g. relative visible cells). This isolates planning/memory from visual-recognition errors. This is NOT an RGB-VLM experiment. A separate follow-up study may introduce RGB partial observations and a vision-language model.

<b>Low-level control:</b> Preferred design is a shared deterministic action executor capable of short, local actions based only on currently observed or agent-maintained maps. The LLM chooses a high-level aim, such as explore\_frontier, approach\_known\_object, interact, or reobserve; a bounded controller executes primitive actions. The controller must not maintain an undisclosed, privileged global map or secretly give an advantage to one condition. Log controller decisions, trajectories and replanning. If controller fairness cannot be established, fall back to one LLM primitive action per decision with smaller pilot sizes.

<b>World modification (distinct experimental extension, not part of standard BabyAI):</b> After standard benchmarks pass, implement a deterministic test wrapper supporting (a) observation-mask/dropout, (b) delayed re-observation after reaching other cells, and (c) pre-specified relocation of an unobserved object to a reachable free cell. Do not make tasks impossible; do not move objects into walls or into the agent; validate goal reachability and the mission's original success criterion after every modification. Record every intervention in evaluator-only ground-truth logs. Avoid silent environment changes that invalidate a benchmark's original task semantics; label modified scenarios as EmbodiedMind custom conditions.

## G. The memory architecture

<b>Core components</b>

1. <b>Episodic store:</b> Append-only observation/action/outcome events with episode\_id, step, modality, source, and observed content. Historical events are never silently overwritten.
2. <b>Spatial/semantic map:</b> Agent-discovered cells and object registry in a consistent relative coordinate frame, including last observed positions, map uncertainty, and encountered doors/walls. Track orientation via public direction and movement via action outcomes; do NOT initialize from simulator ground truth.
3. <b>Belief/evidence ledger:</b> Per-fact status UNSEEN, OBSERVED, INFERRED, STALE, or CONTRADICTED; include provenance, step last observed, evidence links, and reason for invalidation. In v1 do not present arbitrary probabilities as calibrated Bayesian confidence.
4. <b>Working memory:</b> Compact mission, current subgoal, immediate constraints, attempted actions and unresolved questions.
5. <b>Selective retrieval/consolidation:</b> Convert repeated observations into one map fact while retaining raw events. Retrieve relevant entries by mission, location, recency, unresolved conflicts and action need. Keep prompt budgets identical or report a budget-matched secondary comparison.

<b>Canonical fact fields:</b> entity\_id; attribute; value; source\_event\_ids; observed\_at\_step; updated\_at\_step; evidence\_status; contradicts\_fact\_id; last\_verified\_step; retrieval\_relevance. New observations supersede active claims but don't erase old evidence.

<b>Processing pipeline:</b> observe → validate sensor adapter → append event → update local odometry/map → run evidence-revision rules → retrieve relevant beliefs → compose bounded LLM prompt → propose action → validate action → execute → append result.

<b>Belief theory:</b> A full POMDP agent maintains $b_t(s)=P(s_t=s \mid o_{0:t},a_{0:t-1})$. The v1 evidence ledger is a bounded, practical approximation to epistemic bookkeeping; DO NOT call it an exact posterior. A later extension could use a correctly specified transition and observation model for Bayesian updates.

<b>Forgetting policy:</b> Forget/invalidate as an active planning claim, but retain historical records for audit. Never turn “last seen at A” into “currently definitely at A” without recent supporting evidence.

## H. Agent configurations and fairness

| Condition | What is available to the SAME frozen LLM |
| --- | --- |
| <b>B0 Reactive</b> | Current legitimate observation + mission + minimal short-term controller state; no persistent world memory |
| <b>B1 Text history</b> | Same current observation and task + a bounded factual natural-language log/summary |
| <b>B2 Structured, no revision</b> | Episodic events + spatial/object registry, but no explicit stale/contradiction update |
| <b>B3 Full hybrid</b> | Episodic + spatial + belief/evidence revision + compact working memory and retrieval |

Optional diagnostic controls: deterministic non-LLM explorer; privileged full-observation planner strictly labeled ORACLE UPPER BOUND (not a fair baseline); B3 minus selective retrieval; B3 minus provenance timestamps.

<b>Controls:</b> Same LLM version, quantization, prompts except memory payload, generation settings (temperature as close to deterministic as supported), action schema, permitted observations, max steps, decision frequency, controller, validation logic, and precommitted evaluation seeds. Text-baseline memory must receive a fair context/token budget or token counts must be reported and budget-matched comparison added.

## I. Learning methods and what the agent actually learns

<b>Core study uses frozen LLM parameters.</b> Learning means <i>within-episode adaptation</i>: storing observations, identifying object locations, revising beliefs and changing plans. The LLM is not fine-tuned and no gradient-based RL policy is trained for the core benchmark.

<b>Follow-on experiments, only after core results:</b> (i) across-episode strategy memory tested with disjoint world/mission splits and explicit reset boundaries, (ii) schema extraction/one-shot task adaptation, (iii) imitation learning using expert trajectories, (iv) LoRA or RL policy learning, (v) image-based VLM inputs, (vi) energy-constrained/homeostatic agents inspired by CaCTüS Project 7. Do not mix these extensions into the primary experiment.

## J. Experimental protocol

<b>Preflight:</b> Build deterministic observation and action tests before any LLM is connected. Establish a deterministic scripted and/or random control to verify scoring and termination.

<b>Pilot:</b> Five paired seeds per built-in level for each tested variant, focusing on execution correctness, logging, token consumption, and discovery of bugs. Pilot outcomes are engineering diagnostics, not publishable evidence.

<b>Main static benchmark:</b> Evaluate 30 held-out paired seeds in each of DoorKey and GoToObjMaze across B0–B3, for 240 planned condition-by-seed episodes before any retries or preregistered repeats. Apply prespecified episode limits and a shared controller and action budget. Keep development and test seeds disjoint (example dev 0–19, test 1000–1029). Report actual n, exclusions and incomplete cells at each checkpoint. Resume outstanding work under the frozen protocol across run windows.

<b>Dynamic benchmark:</b> After the static and wrapper gates pass, evaluate B1, B2 and B3 on matched held-out seeds for no change, sensory dropout and hidden relocation. Before dynamic scoring, preregister the paired seed count and roster, intervention sequence or trigger, relocation rule, reachability checks and treatment of missing or invalid cells. Match interventions across variants and avoid tuning on held-out outcomes.

<b>Logging:</b> Run manifest, Git commit, OS, Python/packages, model file/digest, quantization, inference configuration, seed, env ID, task text, variant, step count, observations shown to model, memory retrieved, LLM input/output, action validation, world intervention (evaluator-only), reward, success, failure type, token/time totals. Store as JSONL/CSV with optional replay GIF/MP4.

<b>Ground-truth isolation:</b> Separate agent and evaluator processes/interfaces. The evaluator may inspect full hidden states to grade; the LLM, memory module and controller must never see full\_state, unwrapped.grid, undiscovered object positions or privileged success labels before the end of an episode. Test with a deliberate hidden-map contamination test.

## K. Outcome measures and analysis

<b>Primary:</b> Mission success rate on paired held-out seeds; difference between B3 and B1, and B3 and B2.

<b>Secondary:</b> Primitive steps to success; normalized excess path length when a valid shortest path can be calculated; LLM decisions/episode; tokens/episode; compute latency; invalid actions; unnecessary exploration; number of stale-belief actions; post-contradiction recovery rate; time/steps to recovery; hallucinated fact rate (unsupported claims about unseen objects); coverage and map/object-registry errors.

<b>Definitions:</b> A stale-belief action is an action justified by a recorded fact whose assertion has been contradicted by an earlier observation the agent was allowed to receive. An unsupported claim is a positive factual assertion about a world property without corresponding legitimate evidence. Avoid counting unknown targets as hallucinations.

<b>Analysis:</b> Display per-condition means and uncertainty, paired seed-level success differences, 95% paired bootstrap confidence intervals when sample size supports them, descriptive breakdowns by task and intervention, and several failure traces. Pre-register primary comparison to avoid cherry-picking. Use multiple inference repeats if nondeterminism persists even with seeded generation. Treat tiny pilot sample sizes as illustrative.

<b>Negative results are valid:</b> If text history beats structured memory, report why (navigation overhead, map errors, context budgets, mistaken updates). Never fabricate benchmark numbers or state “significant” without testing.

## L. Tooling, computing and reproducibility

<b>Compute:</b> User's Windows RTX 5070 Ti laptop with 12 GB VRAM; local 3B-class text LLM via Ollama, for example [Qwen2.5 3B Instruct](https://ollama.com/library/qwen2.5%3A3b-instruct). Pin digest and quantization. GPU runs inference; CPU runs MiniGrid. Linux/WSL2 is preferred because upstream MiniGrid Windows support is not officially guaranteed.

<b>Software:</b> Python 3.11+, MiniGrid, Gymnasium, Ollama local API, pytest, numpy, pandas, matplotlib, optional scipy. Lock versions after smoke test. Use no cloud API or external paid inference for the core experiment.

<b>Suggested repo layout:</b>

The companion roadmap's active Phase 0 scaffold records the later modular layout and the single <code>uv</code> lock proposed in the CaCTüS strategy discussion. The original sketch follows for reference.

```txt
embodiedmind/
  README.md
  AGENT_GUIDE.md
  RESEARCH_PROPOSAL.md
  requirements.lock
  configs/{pilot,static,dynamic}.yaml
  src/embodiedmind/{envs,observations,memory,agents,planner,controller,evaluation,cli}.py
  tests/{test_observations,test_memory,test_no_leak,test_world_invariants,test_replay}.py
  experiments/manifests/
  results/{raw,processed,figures,replays}/
  reports/{pilot_report,technical_report}.md
  STATUS.md
  DECISIONS.md
  FAILURES.md
```

<b>Reproducibility requirement:</b> Every reported result must be traceable to a config, Git commit, seed list, environment version, model identifier, and raw event log. Do not overwrite earlier benchmark outputs; assign immutable run IDs.

## M. Phases, outputs and finish criteria

| Phase | Artifact | Exit criterion |
| --- | --- | --- |
| 0. Scope, preregistration and scaffold | Versioned protocol, seed policy, check logs and initial scaffold commit | Design is internally consistent and the checked scaffold is committed |
| 1. Infrastructure | Reproducible environment runner and smoke test | Correct reset/step/termination; no hidden state leakage |
| 2. Perception/action interfaces | Observation encoder and action validator | Unit tests pass on deterministic fixtures |
| 3. Memory and baselines | B0–B3 implementations | Replay tests, contradiction tests and prompt-budget accounting pass |
| 4. Integration | Local LLM agent and orchestration | Fully automated end-to-end episode works and logs |
| 5. Pilot | Paired exploratory runs | No crashes, artifacts and failure traces produced |
| 6. Controlled benchmark | Static held-out and custom dynamic runs | Frozen paired coverage achieved and exclusions documented under the prespecified rules |
| 7. Reporting | Results, figures, discussion, limitations | Every numerical claim backed by logs and reproducible scripts |

<b>Engineering milestone (MVP):</b> A stranger can run the setup from the README. B0–B3 execute on the same seeded missions, results are traceable, test leakage is ruled out, and the pilot documents limitations and an observed failure case. More environments and paper publication are stretch goals.

<b>Full experiment completion:</b> Finish the development pilot, the planned static held-out roster, the preregistered matched dynamic roster, and the reproducible analysis and evidence package. A cutoff or resource limit triggers a resumable checkpoint. Keep partial coverage explicit and keep the full experiment open until the scientific acceptance checks pass.

## N. Risk register and stop rules

- <b>Risk: over-scoping.</b> Mitigation: freeze v1 to symbolic MiniGrid; omit VLM, real robots, manipulation, LoRA, intrinsic rewards and multi-agent tasks.
- <b>Risk: untrustworthy navigation baseline.</b> Mitigation: identical shared controller, explicit action logs; report controller dependence.
- <b>Risk: fake certainty.</b> Mitigation: evidence-state tags instead of made-up probabilities.
- <b>Risk: test contamination.</b> Mitigation: privileged state in evaluator only, sealed test seeds, assertions in CI.
- <b>Risk: dynamic modifications break tasks.</b> Mitigation: reachability and success-criterion invariants; drop invalid trials before evaluation by pre-specified rule.
- <b>Risk: model stalls or hallucinated tool calls.</b> Mitigation: strict JSON schema, validation, retries capped uniformly, hard step/call budgets.
- <b>Risk: high inference cost.</b> Mitigation: use a small quantized LLM, bounded prompt, high-level decisions and short deterministic motion macros.
- <b>Risk: rushed application.</b> Keep the CaCTüS application deadline <date start="2026-11-16" />. Checkpoint research when necessary and resume the outstanding work within the authorized run window.

## O. Planned deliverables and claims policy

Deliverables: open-source repository (if user approves publication), tested source code, experiment configuration, baseline comparisons, anonymized logs, plots with uncertainty, short technical report and demonstration replay(s). The experiment is <i>proposed</i> until run. Do NOT claim a result, paper, new algorithm, lab endorsement, or verified improvement in the CV/application unless there is real supporting evidence. In a statement, label it a <b>self-initiated controlled pilot inspired by questions in agent memory and embodied cognition</b>.

<b>Practical next action:</b> Open the companion Agent Runbook, implement Phase 0 → 1, and use its gates before advancing.

## P. Scientific controls for unattended execution

Use the <mention url="https://app.notion.com/p/417f975653bf81e3a17ee53d1430006e">EmbodiedMind — Agent Roadmap & Research Execution Guide (v1.0)</mention> for the Phase 0 scaffold commit, operational gates 0–9, live checklists, and overnight handoff. The phase table in section M summarizes research milestones. This protocol is recorded on <date start="2026-11-14" />.

### Freeze before measurement

- Phase 0 records H1–H4, B0–B3, outcomes and operational definitions, claim limits, seed partitions, common limits and the planned comparisons in a versioned record. Before any held-out run, commit the exact model digest and quantization, software and backend settings, prompt templates and generation parameters, memory rules, observation adapter, action schema, controller and fallback, evaluator, metric definitions, exclusion/retry rules, seed/mission roster, and frozen config hashes. Keep development and held-out seeds disjoint. Seal each custom dynamic condition and its intervention plan before scoring it.
- Keep the proposal's shared controls across conditions, including equal context, action and inference budgets, apart from the intended memory treatment. Use the same seeded task and, for custom comparisons, matched interventions. Agent, memory, controller, and model consume only legitimate partial observations and permitted action history. Keep intervention details, privileged state, evaluator artifacts, and held-out results outside the agent's inputs and development feedback. Test this boundary before inference and again before scored comparisons.
- The serial and parallel Ollama calibration runs use development inputs. Freeze the approved concurrency/backend profile for a scored comparison and apply it across conditions. Record effective device placement, concurrency, request timing and any differences from serial behavior. If resource pressure changes the profile, close the affected batch, retain its outputs and rerun an affected comparison as a complete paired batch under one profile. Amend and version the protocol before any methodological change. Use fresh disjoint held-out data for a revised design if the earlier held-out outcomes influenced that revision.

### Retain evidence and qualify claims

- Preserve immutable run IDs, source commits, config hashes, raw agent-visible traces, model requests/responses, evaluator-only logs, scoring output, raw failure cases, and checksummed artifact inventories. Generate tables, graphs with uncertainty where supported, screenshots and replays from logged runs. Record figure inputs, aggregation code and commands. Identify the seed, variant, run ID and step in visual evidence. Keep evaluator renderings private and outside the agent's inputs.
- Retain valid task failures, timeouts under the fixed episode budget, null and adverse results. Record infrastructure faults, invalid worlds, missing cells and exclusions with their prespecified reason, before looking at outcomes when possible. Report attempted, valid, excluded and linked rerun counts, actual per-condition and matched n, and any incompleteness. Keep unmatched results visible in the coverage record and apply the frozen paired analysis rules.
- A development smoke trace verifies the interface. A paired development pilot supports feasibility and failure characterization. Claims about memory benefits require valid, frozen held-out comparisons and supporting uncertainty. Keep static and custom dynamic results identified, include limitations and negative findings, and keep the application deadline ahead of research extensions.
