# EmbodiedMind agent instructions

## Record every Codex run

- Before the final reply, write one Markdown record under the repo-root `codex-runs/` directory. Use `YYYY-MM-DD-HHMMSS-short-task.md` with a timestamp in the user's time zone. Continue the same record if resuming the same run. Record read-only, interrupted, and blocked runs too.
- Record the user objective, every file or external record changed, and what changed in each. Include the branch and relevant commit hashes, or identify changes still in the working tree. For an unchanged run, record the result and any pending work.
- Document the rationale for material decisions with the evidence, assumptions, alternatives considered, and trade-offs that affected the choice. Include verification commands and outcomes, observed failures and fixes, and anything still unverified. Keep credentials and private data out of the record.
- Keep these records eligible for Git. Use `outputs/` for raw experiment data and link to the relevant archive from the Markdown record.

## Archive every run

- Use one repo-root `outputs/<run-id>/` directory for every new EmbodiedMind run, including smoke tests, calibration, pilots, benchmarks, and saved exploratory runs. Use explicit output paths with the current tools. For interactive runs, save exploratory evidence in its own archive. Resume under the original run ID and preserve earlier attempts.
- Write the run manifest and raw data as the run progresses. Include the source commit, resolved configuration and hashes, software and model versions and digest, commands, seeds, conditions, planned jobs, timestamps, runtime settings, and exit status. For each episode retain exact observations, prompts and responses, memory retrieval and revisions, route hints, chosen and executed actions, movement and reward, termination reasons, tokens, timing, and evaluator-only records. Keep evaluator data outside the agent inputs.
- After every run or checkpoint, including failures and interruptions, preserve raw trajectories, attempt logs, and episode summaries. Generate applicable per-step and per-episode tables, paired comparisons, graphs, screenshots, replays, and a report from the saved evidence. Record unavailable artifacts and the reason, coverage and remaining jobs, and a SHA-256 artifact index. Verify readability and checksums before marking the archive complete. Rerun failed packaging from the existing data.
- Keep `outputs/` eligible for Git, including raw data, run logs, and generated evidence. Keep credentials and unrelated private files out of run artifacts. At the run checkpoint, confirm evidence is visible to Git, review it, and include the run archive in the appropriate local commit. Follow the repository's existing authorization for pushing or publishing.
- Record the output folder, commit, run status, and evidence in the Notion agent roadmap. Use the existing local checkpoint journal when Notion is unavailable and reconcile it when access returns.

## Archive every episode and attempt

- Create `outputs/<run-id>/episodes/<episode-id>/` for each episode. Preserve its finalized record and keep a distinct attempt ID and raw files for every retry, crash, timeout, exclusion, or interruption. Include failed episodes and record never-started episodes in the run roster.
- Write the initial state and every step at native resolution as the episode runs. Retain pre- and post-action observations, exact hints and model input/output, memory facts and revisions, chosen and executed actions, alignment between actions and observations, reward, movement, termination, token counts, latency, and errors. Keep ground truth, interventions, and evaluator-only board state in a separate record outside model inputs.
- Keep each episode's summary, per-step data, available stdout/stderr, and screenshots and replay where reconstruction is possible. Record missing fields or visuals and the reason. Preserve partial traces as written and avoid downsampling raw evidence. Link all episode and attempt files to the run coverage and SHA-256 index.
