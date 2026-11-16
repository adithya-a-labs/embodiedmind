# Diagnose why B0 did better on DoorKey

Retrospective record. Reconstructed from this chat, Git history, and cited evidence. Related follow-up turns are grouped by task.

## Changes

Read all 120 held-out DoorKey traces, counted outcomes and blocked moves, and compared all four agents on seed 1015. No repository files changed.

## Rationale

Used observed behavior to explain where runs failed. The traces support that memory variants repeatedly attempted blocked moves. They leave the underlying cause of those model decisions uncertain.

## Verification and evidence

B0 had 0 blocked moves across 881 actions. B1, B2 and B3 had 339, 647 and 349 respectively. On seed 1015 all agents picked up the key on action 4, and B0 alone finished. [Local static traces](../results/runs/embodiedmind-20261114-0428-ist/static/episodes/)
