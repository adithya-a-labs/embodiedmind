# Agent architecture and ablations

A fresh policy is constructed for each episode. The observation adapter converts MiniGrid’s public observation to a symbolic view, mission and carrying information. The runner feeds the policy current observations and observed movement outcomes. Memory variants can preserve a bounded text history or derive spatial facts in an episode-local coordinate system. Local route hints in the original study use the current view. Later controllers can plan on an observed map.

In model-backed arms the runner assembles a prompt and sends it to loopback Ollama. The proposal is validated and resolved to one primitive step. Later arms can override a proposal with a grounded route or interaction. The primitive controller executes the action and returns the resulting observation. The runner separately saves the full simulator board and intervention state for scoring and visualization.

[Observation adapter](../src/embodiedmind/environments/observation_adapter.py) · [Memory implementations](../src/embodiedmind/memory) · [Proposal resolution](../src/embodiedmind/reasoning/grounding.py) · [Episode runner](../src/embodiedmind/experiments/runner.py)

## Original memory comparison

| Variant | Policy input and memory |
| --- | --- |
| B0 | Current observation and shared route hint, with an empty memory payload. |
| B1 | Bounded text history of prior observations and actions. |
| B2 | Structured episodic and spatial evidence with retrieval and no explicit contradiction revision. |
| B3 | Structured memory with a belief ledger, contradiction updates, aging and working memory. |

The original study shares the primitive action interface and inference settings. B0G and B3G are development controls with the same visible-obstacle guard applied to B0 and B3. [Original protocol](../experiments/manifests/frozen-protocol.md)

## Grounded planning and task memory

| Variant | Addition |
| --- | --- |
| B4 | Retrieves evidence for the current subgoal. |
| B5 | Resolves `approach`, `verify` and `explore` proposals against the observed map. |
| B6 | Adds an episode-independent DoorKey routine extracted from successful development traces. |
| B7 | Uses a handwritten DoorKey routine as a comparator to B6. |
| B8 | Tracks the observed hallway cue and uses guarded forward exploration. |
| B9N | Progress-aware navigation control. |
| B9 | Adds observation-grounded subgoal and interaction state for hallway recall, KeyCorridor and placement tasks. |
| B10 | Grounds mission roles from observations, commits to exploration destinations and checks interaction preconditions. |

B6 uses the [versioned workflow library](../configs/workflows.json). Build a new library with `.venv/bin/embodiedmind learn-workflows RUN_DIR --output NEW_LIBRARY.json`. The library records provenance, and evaluation seeds must be disjoint from extraction seeds.

## B11 mechanism arms

| Arm | Semantic memory | Verification | Proposal source |
| --- | --- | --- | --- |
| B11T | Bounded text for the model, live semantic facts for the controller | Fixed | Ollama |
| B11P | Passive structured | Fixed | Ollama |
| B11R | Revising structured | Fixed | Ollama |
| B11PA | Passive structured | Adaptive | Ollama |
| B11 | Revising structured | Adaptive | Ollama |
| B11C | Revising structured | Adaptive | Deterministic explore proposal |

Revising arms can retract a remembered target claim when the location is observed empty. Masked and unseen cells supply no evidence of absence. B11 revising arms disable evidence aging as a revision mechanism. Adaptive verification can check a hidden claim at least two decisions old using a side glance or a route of up to four actions. Fixed verification requires a facing pose within one planned action. Each policy can take up to four explicit verification actions. The evaluator records separately whether those actions bring the target location into view.

B11 arms share an observation-grounded executor. Route geometry and live interaction preconditions are available to it across arms. Remembered semantic targets depend on the arm’s memory interface. B11C uses the same resolution path and skips per-decision model inference. The campaign runner still verifies the configured Ollama model when starting a roster.

[Agent registry](../src/embodiedmind/agents/__init__.py) · [B11 implementation](../src/embodiedmind/agents/evidence_memory.py) · [Registered comparisons](../experiments/manifests/b11-protocol.md)
