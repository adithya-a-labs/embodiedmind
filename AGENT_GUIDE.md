<!-- Source: https://app.notion.com/p/417f975653bf81e3a17ee53d1430006e | snapshot 2026-11-14 IST | v1.0 with full-study amendment -->

## LIVE EXECUTION CHECKPOINT — 14 November 2026 (04:02 IST)

<callout icon="✅" color="green_bg">
CURRENT STATE: Infrastructure + local GPU inference operational according to user-reported setup and pasted Ollama output. First LLM-controlled BabyAI episode <b>NOT YET VERIFIED</b>. The executing agent must inspect the actual workspace before marking any implementation gate as passed.
</callout>

<b>Machine:</b> ASUS ROG Zephyrus G14, Windows 11; Ubuntu 22.04.5 on WSL2 as \`adithyaa\`; RTX 5070 Ti 12 GB. Preserve system Python 3.10.12 (ROS 2 Humble); use \`uv\` project Python 3.12.16 and \`/home/adithyaa/Projects/EmbodiedMind/.venv\`.

<b>Verified from pasted local command output:</b> \`ollama pull qwen2.5:3b-instruct\` succeeded; \`ollama run ... "Respond with READY"\` printed \`READY\`; \`ollama ps\` reported model ID \`357c53fb659c\`, loaded 2.2 GB, \`100% GPU\`, context \`4096\`, llama.cpp runner. Ollama version \`0.40.16\` and service active at \`127.0.0.1:11434\` are user-reported. A later Ollama JSON API test was reported “done” by the user, without output log.

<b>User-reported operational:</b> WSL password/sudo recovered; dpkg/apt repair succeeded; MiniGrid/BabyAI installed and initial smoke test completed; workspace and virtualenv exist. Some 602 available Ubuntu package updates were noted, but full upgrade was NOT confirmed; do not run disruptive global upgrades during research without need.

<b>Not verified:</b> exact MiniGrid package versions, command output of env smoke test, PyTorch CUDA matmul, Stable-Baselines3, SB3-Contrib, TensorBoard, Docker integration, GitHub remote/auth, Codex CLI, existing repo files or current Git commit, first agent episode, any trained model, any result graph.

<b>Current phase/gate (provisional):</b> Phase 1 infrastructure partially meets intent based on user report; Phase 4 local Ollama connectivity preliminarily verified; <b>Phases 2–9 and ALL research results unverified</b>. Phase 0 protocol documented in Notion but local copies, seed freeze and repo manifest still need inspection. Do not mark Gate 1 complete solely from a one-environment smoke report. Previous “NOT STARTED” notice was the page's initial state and is superseded by this live checkpoint.

<b>Canonical baselines remain FOUR</b> (B0, B1, B2, B3). Do not silently reduce to the three variants mentioned in the separate machine-setup summary.

### Immediate agent work order (resume from evidence)

Begin with the checked scaffold commit in Phase 0. Then work through the infrastructure and observation gates before the first autonomous development smoke.

- [x] User-reported: WSL Ubuntu + isolated Python setup, native Linux workspace and MiniGrid smoke test.
- [x] User-provided output: Qwen2.5 3B downloaded, generated \`READY\`, and loaded on \`100% GPU\`.
- [x] User-confirmed: initial local Ollama JSON API test finished (“done”); return body not logged in conversation.
- [ ] Inspect \`\~/Projects/EmbodiedMind\`; list files and Git status. Do not assume \`first\_llm\_[episode.py](http://episode.py)\` exists.
- [ ] Record \`python --version\`, \`pip show minigrid gymnasium\`, \`ollama list\`, \`ollama ps\`; pin model manifest/digest and dependencies in run manifest.
- [ ] Confirm Ollama local structured JSON response via repeatable logged test; no need to reinstall it.
- [ ] Verify observation orientation, 7×7 ego-grid decoding, legal action mapping and lack of privileged state.
- [ ] Create/repair the minimal \`first\_llm\_[episode.py](http://episode.py)\` if not already present; an example was supplied in chat but no execution evidence exists.
- [ ] Run ONE seeded \`BabyAI-GoToObjS6-v1\` episode with frozen Qwen2.5 3B and no memory; save JSONL and exact outcome.
- [ ] Add unit/smoke tests for invalid outputs and partial observation; ensure no world-state leak.
- [ ] Only then implement B1 text memory, B2 structured memory without revision, B3 full hybrid with revision.
- [ ] Defer PyTorch training, SB3, recurrent PPO, Docker and extra simulators unless directly needed for the next acceptance criterion.
- [ ] Record outcomes, errors, commands and status in \`[STATUS.md](http://STATUS.md)\`, \`[DECISIONS.md](http://DECISIONS.md)\`, \`[FAILURES.md](http://FAILURES.md)\` and link the relevant commit and log.

### Safe resume commands (WSL terminal)

```bash
cd ~/Projects/EmbodiedMind
source .venv/bin/activate
pwd
python --version
python -m pip show minigrid gymnasium
ollama list
ollama ps
git status --short
ls -la
```

Do not fail the phase solely because \`python -m pip\` is missing under an uv-managed environment: use \`uv pip list\` or \`uv pip show\` as appropriate. The commands above are verification suggestions, not confirmed outputs.

### First experiment acceptance check

A first autonomous-episode gate <b>PASSES</b> only when: (1) exact env reset/seed/mission is logged; (2) 7×7 partial observations are decoded correctly, with unseen cells remaining unknown; (3) LLM actions are schema-validated and executed by MiniGrid; (4) no full world state leaks into agent/controller; (5) JSONL trajectory and reward/termination outcome saved; (6) exact model config and source revision recorded. Agent success is NOT strictly necessary; a logged failed episode can satisfy orchestration verification.

<b>Hard next action:</b> Verify and commit the Phase 0 scaffold. Pass the infrastructure and observation/action gates, then execute the first frozen-LLM BabyAI smoke episode and preserve its trace. Record the actual outcome.

---

<callout icon="🔬" color="gray_bg">
Scientific source of truth: <mention url="https://app.notion.com/p/417f975653bf81afa292d347c362b39d">EmbodiedMind — Full Research Proposal (v1.0)</mention>. Re-read before changing hypotheses, baselines, environment behavior, evaluation or reporting.
</callout>

<callout icon="🧭" color="yellow_bg">
CANONICAL AGENT EXECUTION GUIDE • v1.0 • Created <date start="2026-11-14" /> • Status: ENVIRONMENT AND GPU INFERENCE REPORTED WORKING; AGENT EPISODE PENDING. See live execution checkpoint above. This page governs implementation of EmbodiedMind. READ AT PROJECT START AND BEFORE EVERY PHASE/GATE. Do not mark any work complete without reproducible evidence.
</callout>

<b>Parent opportunity:</b> <mention url="https://app.notion.com/p/3f6f975653bf812aa570e32057608b70">Max Planck Tübingen — CaCTüS</mention>. <b>Companion full research proposal:</b> see linked source-of-truth page above. This guide is a proposed engineering/research protocol, not an assurance of autonomous unattended execution.

<table-of-contents />

## 0. Non-negotiable operating contract for an AI coding agent

<b>Mission:</b> Implement and evaluate a reproducible, fully automated MiniGrid/BabyAI experiment testing whether evidence-grounded structured memory and belief revision improve language-conditioned embodied task performance versus reactive and text-history LLM baselines.

<b>At session start:</b> (1) Read this entire guide and the linked Research Proposal. (2) Read the repository's AGENT\_[GUIDE.md](http://GUIDE.md), [STATUS.md](http://STATUS.md), [DECISIONS.md](http://DECISIONS.md) and [FAILURES.md](http://FAILURES.md). (3) Inspect current source code and test output, not just summaries. (4) Identify the first incomplete gate. (5) Announce the immediate task and acceptance test. (6) Implement, test, commit/log evidence, and repeat. If connector access to Notion is absent, use a current exported, versioned copy of these pages in the repository; do not claim a Notion reread occurred.

<b>At each phase boundary:</b> Re-read the relevant heading and the proposal's hypotheses, world contract, baseline controls, and integrity rules. Compare actual artifacts to acceptance criteria. Never skip a gate because code “looks right.”

Use §20 for unattended scheduling, live Notion checkpoints, Git commits, evidence capture, and handoff. Use the phase checklists below for acceptance.

<b>What is forbidden:</b> Fabricating metrics, pretending an experiment ran, adding hidden state to prompts, tuning on held-out test seeds, conflating simulation with physical robot deployment, using different LLM/controller settings across conditions, silently changing hypotheses after seeing results, and modifying the research question solely to make outcomes positive.

<b>Autonomy rule:</b> Continue normal debugging and incremental implementation without asking the user to make trivial choices. Stop and report if a methodological change would alter the hypothesis, comparison fairness, data provenance, or main research claim. Never start an unapproved external publication or send emails to CaCTüS supervisors.

## 1. Canonical decisions and current scope

| Decision | Version 1.0 value |
| --- | --- |
| Study | EmbodiedMind, evidence-grounded memory in embodied LLM agents |
| Primary environment | MiniGrid + BabyAI |
| First runnable test | BabyAI-GoToObjS6-v1 |
| Primary benchmarks | MiniGrid-DoorKey-8x8-v0; BabyAI-GoToObjMazeS7-v0 |
| Physical realism | Abstract 2D grid; explicitly not real robot dynamics |
| Input modality | Symbolic 7×7 partial observation converted to accurate compact text |
| Local LLM | Qwen2.5 3B Instruct quantized via Ollama (verify and pin exact model/digest) |
| Learning | Frozen LLM; online memory/belief updates, not weight training |
| Conditions | B0 Reactive; B1 Text history; B2 Structured/no revision; B3 Hybrid/revision |
| Optional future | Real RGB-VLM, cross-episode schemas, homeostasis, RL/LoRA |
| Baseline control | Identical model, observation/action channels, controller, limits and seeds |
| Data policy | Ground truth only for evaluator; test seeds sealed |
| Priority | Complete the full experiment across authorized run windows. Protect the CaCTüS application deadline <date start="2026-11-16" />. |

All these are proposed defaults drawn from the conversation and full proposal. If the user changes one, record a dated decision and evaluate affected tests.

## 2. Success criteria at three levels

<b>Engineering smoke success:</b> Environment resets and steps correctly; valid partial observations; model connection works; action commands validated; event logs and reproducible replays exist; no privileged state leak.

<b>Research pilot success:</b> Four defined variants run on matching mission seeds; primary/secondary metrics are computed from raw trajectories; memory/provenance logic passes unit tests; at least one interpretable failure trace is documented. Pilot is NOT evidence of general superiority.

<b>Full benchmark success:</b> Fixed test seeds, controlled interventions with reachability checks, paired uncertainty estimates, preregistered comparisons, full source/config/model manifests, negative results retained, technical report honest about abstract-world limitations.

## 3. Repository layout to build

### Active Phase 0 scaffold

Use one Python package with a stable <code>python -m embodiedmind.cli</code> entry point. The CaCTüS strategy discussion proposed a modular layout and a single <code>uv</code> lock. Create missing structure during Phase 0 and put implementations in their owning modules as gates advance.

```txt
EmbodiedMind/
  README.md
  AGENT_GUIDE.md
  RESEARCH_PROPOSAL.md
  STATUS.md
  DECISIONS.md
  FAILURES.md
  pyproject.toml
  uv.lock
  .python-version
  .gitignore
  .env.example
  configs/{pilot,static,dynamic,models}.yaml
  src/embodiedmind/
    __init__.py
    cli.py
    environments/{factory,observation_adapter,dynamic_world}.py
    agents/{base,reactive,text_memory,structured,hybrid}.py
    memory/{episodic,spatial,semantic,belief,working,retrieval,consolidation}.py
    reasoning/{llm_client,planner,prompts,action_validator}.py
    control/{controller,navigation}.py
    experiments/{runner,evaluator,metrics,logger,replay}.py
    analysis/{statistics,plots,report}.py
  scripts/
  tests/
  experiments/manifests/
  results/{raw,processed,figures,replays,screenshots}/
  reports/
```

Track package boundaries, scope/config skeletons, setup docs and placeholders for empty output directories. Add substantive modules and script entry points at their gates. Mark stubs as pending and make unfinished commands fail clearly. Use <code>pyproject.toml</code> and a generated <code>uv.lock</code> for this layout. Reuse working files and interfaces in the checkout. Keep the agent-side packages dependent only on permitted inputs, with evaluator state and renderings behind a distinct interface.

### Original layout reference

```txt
embodiedmind/
  README.md                 # setup + exact commands
  AGENT_GUIDE.md            # exported copy of this runbook
  RESEARCH_PROPOSAL.md      # exported copy of canonical proposal
  STATUS.md                 # current phase, gates, evidence links
  DECISIONS.md              # rationale for changed choices
  FAILURES.md               # observed errors + attempts + resolution
  requirements.lock
  configs/
    pilot.yaml
    static.yaml
    dynamic.yaml
  src/embodiedmind/
    __init__.py
    cli.py
    envs.py
    observations.py
    tools.py
    controller.py
    memory.py
    belief.py
    prompts.py
    llm.py
    agents.py
    evaluation.py
    logging_utils.py
  tests/
    test_env_api.py
    test_observation_contract.py
    test_memory.py
    test_belief_revision.py
    test_no_leakage.py
    test_dynamic_reachability.py
    test_replay.py
  experiments/manifests/
  results/raw/
  results/processed/
  results/figures/
  results/replays/
  reports/
```

The earlier layout above records the original interface intent. Build from the active Phase 0 scaffold and keep existing verified interfaces stable.

## 4. Required CLI interface (commands to implement)

Below are desired commands; they are NOT runnable until implemented. The agent must make them work and document actual usage.

```bash
python -m embodiedmind.cli smoke --env BabyAI-GoToObjS6-v1 --seed 42
python -m pytest -q
python -m embodiedmind.cli run --config configs/pilot.yaml
python -m embodiedmind.cli evaluate --manifest experiments/manifests/pilot.json
python -m embodiedmind.cli report --manifest experiments/manifests/pilot.json
```

A smoke command MUST exit nonzero on failed env registration, illegal action mapping, malformed observation, unexpected termination, or missing required artifacts. Print the exact registry and installed version when environment names differ; do not silently substitute a task.

## 5. Phase 0 — Research preflight, scaffold and first commit

- [ ] Inspect the real workspace, Git history/status, repo instructions and author identity. Reuse the existing repository. Initialize Git only if needed. Preserve existing user changes and start work on a project branch such as <code>codex/embodiedmind-overnight</code>.
- [ ] Copy the two canonical Notion pages into <code>AGENT_GUIDE.md</code> and <code>RESEARCH_PROPOSAL.md</code> with source URLs, snapshot timestamp and protocol revision. Create or update <code>README.md</code>, <code>STATUS.md</code>, <code>DECISIONS.md</code> and <code>FAILURES.md</code>. Record the first unverified gate from actual evidence.
- [ ] Materialize the active scaffold in section 3. Create package and config skeletons, script/test/manifest/report directories, ignored run output paths, the Python pin, <code>pyproject.toml</code>, a generated <code>uv.lock</code> and a credential-free <code>.env.example</code>. Keep project Python isolated from system Python. Verify that secrets, private data, model weights, virtualenvs and bulk results are ignored.
- [ ] Write README research question, H1–H4, strict claim boundary, primary endpoints, and exact bootstrap, overnight launch, status, stop and resume commands as they become available. Mark pending commands clearly.
- [ ] Freeze all four variants B0/B1/B2/B3 definitions and common budgets.
- [ ] Record B0–B3 definitions, shared budgets, observation/evaluator boundary and inclusion rules. Seal disjoint development and held-out rosters. If no prior registered partition exists, use the example dev 0–19 and test 1000–1029 after validation. Use seed 42 only as a separate smoke fixture unless the registered development roster includes it. Leave the full implementation and runtime freeze to Gate 5.
- [ ] Define run IDs, config hashes, result paths, budget and cutoff, the artifact index, and the local Notion sync queue. Confirm proposed outcomes are labeled as proposals.
- [ ] Confirm no current result is represented as an observed finding.
- [ ] Check the lock and fresh project setup, package import and CLI help, and the staged diff. Commit the verified scaffold locally before Phase 1, for example <code>chore(repo): scaffold reproducible EmbodiedMind study</code>. If an existing commit already contains the complete scaffold and passes the checks, record its hash and commit only needed updates. Save check logs and the scaffold commit hash in the run checkpoint and Notion.

<b>Gate 0 exit</b> — The scaffold exists under a verified local commit. A fresh checkout can reproduce the documented setup and entry-point checks. The scientific protocol, evidence locations and first pending task are recorded. Connector outages follow the local queue procedure in section 20.2.

## 6. Phase 1 — Install and establish environment

- [ ] Record OS, WSL2/Ubuntu if used, Python, CUDA (if any), GPU driver and Ollama versions.
- [ ] Create isolated Python environment; install Gymnasium, MiniGrid, pytest, numpy, pandas, matplotlib; pin versions after success.
- [ ] Verify official registry names with documentation or installed registry.
- [ ] Reset and step BabyAI-GoToObjS6-v1, MiniGrid-DoorKey-8x8-v0 and BabyAI-GoToObjMazeS7-v0 using fixed seeds.
- [ ] Inspect returned observation, action space, reward, termination and truncation.
- [ ] Ensure headless batch runs do not require graphical desktop; save one optional debug visualization.
- [ ] Implement first smoke CLI and short READMEs.

<b>Gate 1 exit:</b> Three official envs run to termination or cap; deterministic reset works; no crash; seed and mission logged.

<b>Fallback:</b> If dependency on native Windows fails, switch to WSL2; log decision. If env ID changed, document verified mapping rather than inventing a replacement.

## 7. Phase 2 — Observation integrity and action validation

- [ ] Implement ObservationAdapter using ONLY observation dictionary returned by env (7×7×3 ego grid, direction, mission); decode object/color/state via official mappings.
- [ ] Add local coordinate convention; maintain agent-relative orientation and position using allowed action history, not hidden simulator pose.
- [ ] Represent not-yet-seen cells as UNKNOWN; do not conflate unseen, empty and occluded.
- [ ] Implement schema-validated primitive actions and allowed local macro actions. Same shared controller across baselines.
- [ ] Prove controller does NOT read unwrapped.grid, hidden target position, global agent position or privileged reward.
- [ ] Implement tests for wall blocking, rotation, pickup/toggle success feedback, occlusion and unknown cells.

<b>Gate 2 exit:</b> Golden observation fixtures decode exactly; secret wall/object location is absent from prompts and memory; malformed action rejected; path/controller has no hidden-map channel.

Next, connect the first frozen-LLM GoToObj development smoke to the verified observation and action path. Capture its JSONL, model digest and outcome under the First experiment acceptance check above before B1–B3 integration.

<b>Red flag:</b> RGBImgObsWrapper/FullyObsWrapper can expose entire maps—do not use full-observation wrappers for agent input. Visualizations or evaluator-only diagnostics must be isolated.

## 8. Phase 3 — Memory engine and deterministic tests

<b>Required stores:</b> EpisodicLog (append-only), SpatialMap/ObjectRegistry (only observed facts), BeliefLedger (OBSERVED, INFERRED, STALE, CONTRADICTED, UNKNOWN), WorkingMemory (mission, current subgoal, pending action), RetrievalManager (bounded, relevant context).

- [ ] Event fields: episode\_id, step, legitimate\_observation, action, outcome, source\_id, token\_cost.
- [ ] Facts fields: entity, attribute, value, observation source, observed\_at\_step, status, supersedes/contradicts IDs.
- [ ] When an item reappears, consolidate into the active object registry without deleting episodic events.
- [ ] When direct evidence conflicts, invalidate active certainty and mark prior observation superseded, not falsely deleted.
- [ ] Do not infer accurate probability distributions from fabricated percentages.
- [ ] Add unit tests: repeated wall observations; key remembered after leaving FoV; object relocation; stale facts; contradictions; navigation/map consistency; provenance retrieval; event ordering; reset-between-episodes.

<b>Gate 3 exit:</b> All memory tests pass and demonstrate both a remembered fact and a correctly revised contradictory fact. Event history stays intact.

## 9. Phase 4 — Baselines and LLM planner

- [ ] B0: current observation and mission only; no persistent object registry.
- [ ] B1: bounded factual natural-language history/summary and same current observation.
- [ ] B2: episodic + spatial records, WITHOUT active staleness/contradiction logic.
- [ ] B3: episodic + spatial + belief revision + selective retrieval + working memory.
- [ ] Same model digest/quantization/system prompt/action schema; same action validation, controller, environment and budgets.
- [ ] Implement deterministic output parsing: validated JSON action with rationale/provenance fields (do not request hidden chain-of-thought). On invalid outputs, use a fixed, logged fallback applied uniformly.
- [ ] Limit context length, LLM calls, generated output tokens and primitive environment steps; log budget usage.
- [ ] Check that LLM sees no ground-truth data or post-episode score while planning.
- [ ] If model quality is insufficient, document failure before switching models; if switching, restart all comparisons on a newly frozen model.

<b>Gate 4 exit:</b> One end-to-end episode with each variant completes (success OR properly logged failure) and produces a trace of legal commands, memory context and scoring. No baseline-exclusive advantages.

## 10. Phase 5 — Pilot and failure characterization

- [ ] Run five paired development seeds per selected environment/variant. Store exact full config and run IDs.
- [ ] Inspect logs for hallucinated objects, repeated loops, impossible commands, inconsistent odometry, reward leakage, failure to revise memory.
- [ ] Write a short pilot report: tables, actual n, raw failure traces and cost.
- [ ] Fix engineering errors on DEVELOPMENT seeds only; record changed commits, design decisions and rerun diagnostics.
- [ ] Record at least one case where structured memory HELPS, FAILS or makes no difference; do not select only favorable episodes.

<b>Gate 5 exit:</b> The paired pilot can be reproduced, includes observed failures, and supports a method freeze. Before starting held-out scoring, commit the full experimental and runtime freeze required by the proposal, including exclusion/retry rules, config hashes and sealed paired rosters. Record its SHA in both pages. If the pilot or freeze checks fail, finish recovery before opening held-out results.

## 11. Phase 6 — Static held-out benchmark

- [ ] Freeze prompt template, LLM parameters, memory logic, environment versions, controller, action budgets, reporting code and test seeds.
- [ ] Run 30 paired held-out seeds each for DoorKey and GoToObjMaze across B0–B3. Track all 240 planned cells. Resume missing eligible jobs after a cutoff using the frozen config, seed roster and artifact manifest.
- [ ] Check equal seed/task distribution; investigate unmatched/failed episodes without removing them after seeing outcomes.
- [ ] Compute completion rate, steps, invalid actions, token counts, LLM calls, latency and per-seed paired differences.
- [ ] Save immutable output manifest and checksums.
- [ ] Do not tune hyperparameters after inspecting the held-out test results; if revised, create an explicitly new protocol version.

<b>Gate 6 exit:</b> The 30-seed paired roster for each environment is accounted for under the frozen coverage and exclusion rules. Verified results are auditable, including valid episode failures, exclusions and linked retries. Keep the gate open while required runs are outstanding.

## 12. Phase 7 — Custom dynamic / stale-memory benchmark

ONLY start after static environment and memory gates pass.

- [ ] Build a separate labeled custom wrapper; do not silently call it a standard BabyAI benchmark.
- [ ] For sensory dropout, define fixed randomness, probabilities and corruptions. Preserve truthful ground-truth log for evaluator only.
- [ ] For hidden object relocation, move target only out of view into a reachable legal free cell; verify mission remains achievable under original terminal rules.
- [ ] Log event trigger, original and new location in evaluator-only record; NEVER expose coordinates to agent.
- [ ] Create matched pairs for no-change, noise and relocation.
- [ ] Test evidence contradiction recognition, stale-location action counts, re-observation and recovery.
- [ ] Before scoring, freeze the dynamic paired seed count and roster, intervention plan and coverage rules. Run B1/B2/B3 on the matched roster for no change, sensory dropout and hidden relocation. B0 remains an optional diagnostic.
- [ ] Re-verify no hidden-state leakage and no impossible tasks before scoring.

<b>Gate 7 exit:</b> The frozen dynamic roster is complete under the prespecified rules. World invariants, reproducibility and unchanged success semantics are verified. Keep the gate open while required runs are outstanding.

## 13. Phase 8 — Analysis and scientific reporting

- [ ] Primary comparisons: B3–B1 success and B3–B2 stale-action rate.
- [ ] Pair by seed and mission; estimate differences and uncertainty (paired bootstrap 95% intervals where feasible).
- [ ] Stratify results by environment and intervention; avoid reporting only pooled averages.
- [ ] Plot task success, steps, LLM calls, token consumption, hallucination/staleness and post-change recovery.
- [ ] Document representative failures and negative or null findings.
- [ ] Discuss: prompt-token fairness, controller/odometry dependence, synthetic observation limitations, partial-world misidentification, no true VLM/real-world robot, lack of training, insufficient sample size if applicable.
- [ ] Write 2–3 page technical pilot report and README result summary with reproducibility commands and citations.
- [ ] Do not claim new SOTA, physical deployment, formal Bayesian filtering, learned schemas or a peer-reviewed contribution.

<b>Gate 8 exit:</b> Every table and figure can be regenerated from raw logged runs; findings clearly distinguished from hypotheses.

## 14. Phase 9 — Package, freeze and application use

- [ ] Validate all tests and CI; pin dependencies and model info.
- [ ] Ensure GitHub repo is publishable only if user authorizes it; strip secrets and private data.
- [ ] Preserve complete configs/manifests and experiment replays.
- [ ] Write a 100–150-word factual project summary with numbers ONLY if verified.
- [ ] If no experiment finished, describe it as an ongoing independent investigation, not a completed research result.
- [ ] Respect priority of the CaCTüS application deadline <date start="2026-11-16" />; submit the application even if the extension is unfinished.

<b>Gate 9 exit:</b> Gates 0–8 pass. Reproduction instructions and evidence index exist, report claims match the verified results, and the final handoff is reconciled. A partial package records progress and leaves the full experiment open.

## 15. Per-session agent loop — the mandatory self-review

At the beginning AND after each meaningful code change:

1. <b>READ:</b> This runbook + proposal + status + tests; identify current gate.
2. <b>INSPECT:</b> Current branch/commit, files, last run logs, latest error and incomplete criteria.
3. <b>PLAN:</b> Select only the smallest action that advances the current gate. Explain why it's on the critical path.
4. <b>EXECUTE:</b> Make targeted code/doc changes. Never alter test seeds or evaluation logic to hide failures.
5. <b>VERIFY:</b> Execute the gate-specific automated test or smoke run; capture exit code, logs and artifact paths.
6. <b>RECONCILE:</b> Are observations valid, baselines fair, and conclusions supported? If not, record failure and repair.
7. <b>RECORD:</b> Update <code>STATUS.md</code> and the relevant decisions or failure log. Tick verified tasks and mirror meaningful checkpoints to Notion under section 20.2. Queue updates locally during connector outages.
8. <b>CONTINUE OR STOP:</b> Advance dependent work after a gate passes. If a gate is blocked, record the precise failure and continue independent authorized work until the affected gate can resume or the run reaches its cutoff.

<b>Hard stop triggers:</b> unexplained privileged-state access; baseline condition leakage; invalid task success criteria; inability to reproduce pilot; loss of seed/model provenance; unsupported “improved” claims; request to perform external irreversible actions without user authorization.

## 16. [STATUS.md](http://STATUS.md) template and checkpoint protocol

```markdown
# EmbodiedMind Status
Protocol version: v1.0
Current phase: 0 - Research preflight
Current gate: NOT STARTED
Last verified commit: none
Environment & version: not installed
LLM model digest: not pinned
Last passing test: none
Last run manifest: none
Blocked by: none
Next single action: create repo scaffold and pin environment API
Evidence: no experimental runs yet
Claims allowed now: proposed study only
```

After EVERY gate: mark PASS/FAIL with exact command, exit code, timestamps, commit hash, relevant screenshots/logs, and unresolved caveats. This is a living guide, not a pre-checked progress tracker.

## 17. Diagnostics decision tree

| Symptom | Investigation | Allowed next move |
| --- | --- | --- |
| Env doesn't register | Check installed registry and package version | Pin/update verified env identifier and record decision |
| Memory does not help | Inspect baseline fairness, contexts and task difficulty | Report null result; do NOT invent improvement |
| Agent knows unseen objects | Audit prompt fields and wrappers | Stop and fix ground-truth leakage before any benchmark |
| Memory references wrong cell | Audit orientation transform and odometry | Add deterministic movement fixtures |
| Relocation creates impossible goals | Validate legal cell and reachability before action | Drop invalid configuration by preregistered rule; repair generator |
| LLM repeats an action | Inspect tool schema, step budget and observation changes | Apply common uniform fallback; log failure |
| GPU/LLM too slow | Inspect tokens/calls and max\_context | Reduce equally for ALL variants; rerun comparison |
| Evidence contradictory | Verify source event/timestamp + status transitions | Keep raw episodes; invalidate active claims |
| Seeds no longer paired | Audit manifest and config hashes | Stop comparison and rerun paired seeds |
| Notion page unreachable | Inspect local exported AGENT\_[GUIDE.md](http://GUIDE.md) protocol version | Continue against verified local snapshot; disclose Notion sync gap |

## 18. Acceptance checklist for final handoff

- [ ] The exact research question, four hypotheses and limitations are documented.
- [ ] All four agent conditions implemented as specified.
- [ ] Legitimate partial observation enforced by tests.
- [ ] Seeded MiniGrid missions reproduce.
- [ ] Every model/action/memory decision logged.
- [ ] At least one valid paired pilot exists with real data.
- [ ] Charts and results can be regenerated from raw logs.
- [ ] Failure cases and null outcomes included.
- [ ] Report clearly says whether weights were or were not trained.
- [ ] All source papers linked; no false Max Planck endorsement.
- [ ] CaCTüS application remains the higher-priority deadline.

## 19. Reminder to the executing agent

Be a scientific research engineer, not a demo generator. Optimize for <b>correctness, falsifiability and traceability</b>, then speed. When uncertain, return to the research question and the baseline controls. A surprising failure documented carefully is more valuable than a positive metric produced by information leakage.

## 20. Unattended overnight operating protocol

One coordinator owns gate decisions, merges, Git checkpoints, Notion updates and the experiment queue. Coding workers can work in parallel. Each experimental condition B0–B3 runs isolated episodes. This operating protocol is recorded on <date start="2026-11-14" />.

### 20.1 Start and advance the run

1. Read the latest Notion pages or their verified local snapshots. Check Git, project instructions, last clean checkpoint, existing processes, current manifests, access and free resources. Begin at the first incomplete gate. Reuse verified prior work with matching provenance.
2. Record the run ID, coordinator, branch and base SHA, active gate, full-experiment coverage target, cutoff with time zone, time reserved for handoff, and limits for coding tokens or credits, inference, disk, CPU, RAM and GPU. Use the authorized session limits. If the safe budget is unknown, start with bounded checks, measure throughput on development runs, and estimate the time for the remaining roster. Keep the CaCTüS deadline and record any host constraint.
3. Follow gates 0–9 in this guide. At each gate, read its acceptance criteria, execute the gate's actual commands, inspect logs and required artifacts, record a verified checkpoint, commit the coherent changes and reconcile progress. Engineering preparation for later gates may run in parallel. Release a dependent integration or scored run only after prerequisite gates pass.
4. Run the first frozen-LLM GoToObj development smoke after observation/action integrity passes, before spending inference on B1–B3. Finish the memory and baseline gates, run the five-seed-per-environment pilot, freeze the protocol, complete the static held-out roster, then complete the labeled dynamic benchmark with reachability and leakage checks. Finish analysis and packaging. If a cutoff, resource limit or blocker interrupts work, record every open gate, remaining job and the exact resume command. In the next authorized window, reuse validated outputs and continue from the first incomplete gate.
5. A gate passes when each required acceptance check has evidence. Set explicit status <code>Pending</code>, <code>Running</code>, <code>PASS</code>, <code>FAIL</code>, <code>BLOCKED</code> or <code>DEFERRED</code>. A scientifically valid failed episode can satisfy an engineering check. Mark a gated benchmark incomplete when the frozen coverage target was missed.

### 20.2 Maintain live Notion checklists

- In the live tracker below, start each run with the run ID, start/cutoff, branch/base SHA, current gate, owner and next command. Append a compact timestamped journal beneath it. Keep this run's history when opening the next run. Link the proposal's controls when recording the protocol freeze.
- As each task is verified, tick the existing phase checklist item immediately or in the same checkpoint transaction as related checks. Record the stable task/gate ID, status, time, command and exit code or check result, Git SHA, run/attempt ID, evidence link or artifact path, and next action. Keep failed or pending boxes open and annotate the reason. Post meaningful changes, including start, verified task completion, a gate transition, recovery, material budget pressure and final handoff. Mirror meaningful decisions and science milestones to the proposal's progress snapshot.
- Single Notion writer. Keep an append-only local checkpoint journal and pending sync queue keyed by run ID + task/checkpoint ID. Update <code>STATUS.md</code> and, when applicable, <code>DECISIONS.md</code> or <code>FAILURES.md</code>. Use stable IDs and read the target before replaying an uncertain edit. If Notion is unavailable, continue authorized work from the verified snapshots, make each local checkpoint durable, and retry queued edits with bounded backoff. Reconcile in order when access returns. Report the last successful sync and any remaining queue at handoff.
- Attach a durable, private evidence link when available. Record repo-relative paths and an index entry when artifacts are local. Preserve the version and checksums needed to locate them.

### 20.3 Parallel coding and integration

- Use as many concurrent agents as the dependency graph, available slots and measured resources can support productively. Expand when work is independent and shrink when integration, GPU, CPU, memory, context, or budget gets tight. Run serially when only one useful task is ready or the host lacks workers.
- Assign each worker the gate/task ID, base SHA, one branch or worktree, owned files/interfaces, dependencies, acceptance command, expected artifacts and budget. A useful split is interface/adapter tests, memory fixtures and implementations, runner/logging, and offline reporting. Use read-only worker reviews of fairness, leakage and artifacts in parallel with implementation. Give coding workers only development or synthetic data where they can influence design. Keep held-out data scoped to evaluation.
- Keep workers off the same files and resource slots. The coordinator verifies the returned diff, evidence and proposed commit, integrates in dependency order, reruns shared checks and records ownership transfers. Cancel redundant work and reclaim idle slots. For a compact return require changed paths, checks, failures, artifact paths and the next dependency.

### 20.4 Calibrate and control local Ollama concurrency

- Use the existing project model if its digest and quantization verify. Start inference concurrency at one request, with one loaded model and a bounded client queue. When the installed Ollama version supports them, the coordinator may adjust <code>OLLAMA_NUM_PARALLEL</code>, <code>OLLAMA_MAX_LOADED_MODELS</code> and <code>OLLAMA_MAX_QUEUE</code> for a project-owned loopback server. Record the prior settings. Prefer a run-scoped process or a reversible service override on a service the project owns. Drain active work before restarts. Leave other users' jobs alone and keep the endpoint on loopback.
- Run serial dev calibration, then test two slots with the exact frozen request shape and longest expected prompt. Increase one slot at a time only when measured throughput improves and outputs remain comparable. Observe effective slots/context and device placement via server logs and <code>ollama ps</code>. Measure queue time, latency, completed requests or episodes per minute, VRAM/headroom, RAM, thermals, token counts, parse/schema validity and matched development outputs. Budget for extra context memory per concurrent request. Use a single global admission limit with backpressure, and give experiment inference priority over any local coding assistance.
- Step back on overload, repeated 503/timeouts, out-of-memory errors, CPU spill, context truncation, thermal limits, degradation or serial/parallel discrepancies that invalidate comparison. Drain, preserve attempt logs, restore the last verified profile and recheck on dev. Keep one fixed profile within a scored batch and match or interleave paired conditions to limit order, cache and thermal bias. Record runtime changes and restart affected paired comparisons under the same profile. Preserve per-request seeds, model, generation settings, context and fallback behavior across B0–B3. Restore prior service settings at handoff and log the restoration result. [Ollama Local FAQ](https://docs.ollama.com/faq#how-does-ollama-handle-concurrent-requests)

### 20.5 Automate, monitor and spend within limits

- Build and document a versioned project supervisor around the verified test, run, evaluate and report commands, with launch, status, graceful stop and resume. Demonstrate recovery on a bounded dev job before the full benchmark. Use a durable local execution method available on the host, with one active supervisor per run, PID or job ID, independent stdout/stderr, exit codes, heartbeat, timeouts and per-episode checkpoints. A started process is <code>Running</code>. Wait for exit and verify output completeness before checking off a task.
- Store canonical job IDs for protocol/config + environment + split + seed/mission + intervention + variant + replicate. Give retries distinct attempt IDs. Write to temporary files and finalize atomically after validation. Schedule missing eligible jobs on resume and deduplicate intact completed jobs by manifest and checksum. Advance checkpoints from evidence and reconcile orphaned attempts after interruption.
- Monitor heartbeat age, live process and progress counters, pairing coverage, elapsed time, resources, infrastructure failure rate and time to cutoff. Wait on available completion events or poll with backoff sized to the job's expected duration. Budget back from the cutoff for integrity checks, reporting, commit and sync. Stop admitting jobs when the current complete paired batch plus handoff cannot fit, then drain or checkpoint and report planned versus observed coverage.
- Start with deterministic fixtures and compact dev runs. Use headless renders and offline metrics, cache deterministic preprocessing or exact completed outputs under their full provenance, and keep cached model fixtures out of live scored episodes. Cap calls and response lengths uniformly. Batch independent reads and reporting operations. Give workers focused context, reuse short checkpoints and inspect targeted log excerpts in the conversation while keeping full logs on disk. Prefer local compute for core inference and record usage and any measured cost. Paid services require explicit authorization.

### 20.6 Capture and index evidence

- Save a manifest and hashes for each run, resolved config, exact invocation and exit codes, Git SHA and dirty-state indicator, time stamps, dependency lock/version, OS, model digest/quantization, backend, device/concurrency profile, split, seed/mission, condition, intervention, limits and planned versus observed cells. Record per-attempt errors and retry links.
- Retain raw JSONL trajectories: agent-visible observation and memory references, actual model inputs and outputs, parse/validation/fallback, proposed and executed actions, rewards and termination/truncation, and available token/latency totals. Keep intervention and full-state scoring in protected evaluator-only data. Preserve negative, null, aborted and failed cases with their classification.
- Generate per-episode CSV/JSON, paired summaries with actual n and missing cells, plots with source metadata, and representative screenshots and GIF/MP4 replays for success, failure and contradiction when observed. Save PNGs by run/variant/seed/step and generate plots for success, steps, calls/tokens/latency, staleness and recovery where applicable. Keep reproducible headless rendering/export commands. Protect evaluator replay artifacts from agent input and redact credentials/private data before sharing.
- Use the manifest and a checksummed index with path, type, run/attempt, size and provenance. Keep raw outputs immutable. Derive tables and figures from finalized input logs. Spot-check artifact readability, provenance, figure regeneration and failure traces. Write an explicit reason for missing evidence. Large artifacts and sensitive logs stay in ignored private storage with resolvable paths. Commit source, tests, configs, small safe summaries and artifact references.

### 20.7 Commit coherent changes and recover

- Commit the Phase 0 scaffold first. After each verified milestone, and during long phases once a coherent tested change is ready, group related code, tests and docs. Inspect status and staged diff, run scoped checks, stage only owned changes and record the verified hash and evidence in Notion. Use semantic messages such as <code>test(observation): enforce evaluator isolation</code> and <code>feat(runner): resume verified paired episodes</code>. Record gate-level tests after integration. Preserve user edits and branch history. Keep remote pushes and publication within the user's explicit authority.
- For transient service overload or interruption, record the failure, verify it is infrastructure-related, then use bounded retries with backoff under the predeclared rules. A valid task failure counts under the frozen rules. For stalls or crashes, inspect the heartbeat and logs, stop only the run-owned process when required, preserve partial output, and resume from the last verified commit and manifest. Revalidate the affected gate after a repair. Keep quarantined evidence and mark its impact.
- Stop the affected gate for leakage, invalid task semantics, missing provenance, irreproducibility, unfrozen scientific changes, or persistent resource faults. Preserve evidence and continue independent authorized tasks where useful. If a repair follows inspection of held-out outcomes, version the design and use fresh disjoint held-out data for the revised comparison. Record the precise blocker and safe next action.

### 20.8 Live overnight tracker and morning handoff

Run ID / branch / verified SHA / start and cutoff / coordinator / current gate / next command / last Notion sync — update at launch and each meaningful checkpoint. Run pending.

- [ ] Gate 0 — Versioned protocol and scaffold committed and verified.
- [ ] Gate 1 — Pinned environment and official seeded smoke checks.
- [ ] Gate 2 — Observation/action validation and evaluator isolation.
- [ ] Gate 3 — Memory fixtures, reset, provenance and contradiction tests.
- [ ] Gate 4 — Verified autonomous smoke and logged B0–B3 end-to-end episodes.
- [ ] Gate 5 — Paired development pilot, failure report, and committed freeze before held-out.
- [ ] Gate 6 — Auditable static held-out pairs.
- [ ] Gate 7 — Preregistered custom dynamic roster complete, with matching, reachability and invariants verified.
- [ ] Gate 8 — Regenerable analysis, figures, examples and limitations.
- [ ] Gate 9 — All required gates passed, research package verified and final handoff reconciled.

At cutoff or completion, write the same handoff to <code>STATUS.md</code>, the run report and Notion. Record achieved and pending gates, blockers, commits and tests, planned/attempted/valid/excluded/matched episode counts, remaining cells, results with claim limits, failure examples, report and artifact-index paths, usage and cost, service restoration and sync status. At a cutoff, capture the verified partial package, active job state and exact resume command. Resume in the next authorized window with the same frozen benchmark registry and deduplicate completed jobs. Mark the experiment complete only after the required static and dynamic coverage, analysis, evidence package and handoff pass. Include the factual 100–150-word application summary at the packaging gate.
