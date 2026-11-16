# Explain the results, memory architecture, and test worlds

Retrospective record. Reconstructed from this chat, Git history, and cited evidence. Related follow-up turns are grouped by task.

## Changes

Explained the paired results and their limits, showed a seed-2000 relocation step-through, and compared the proposed memory architecture with the frozen implementation. The step-through was saved in the chat workspace. No repository changes were made in these explanation turns.

## Rationale

Used recorded observations and evaluator frames to distinguish what the agent knew from what happened on the board. Separated explicit stale citations from unobserved intent. Verified that B3 used cell-indexed rules and that the runner never supplied a prior intent.

## Verification and evidence

Cross-checked the final report, the saved trajectory, and source at `a44c34e`. [Protocol](../experiments/manifests/frozen-protocol.md)
