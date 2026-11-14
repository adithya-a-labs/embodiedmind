"""Build auditable experiment tables, figures, and a Markdown report from raw outputs."""

import csv
import hashlib
import json
import os
from collections import Counter
from dataclasses import asdict, fields
from pathlib import Path
from statistics import fmean

from embodiedmind.agents import VARIANTS as KNOWN_VARIANTS

from .statistics import METRICS, Comparison, compare, numeric, stratify


EPISODE_FIELDS = (
    "run_id", "job_id", "split", "environment", "seed", "mission",
    "intervention", "variant", "replicate", "status", "outcome", "reason",
    "attempts", "trajectory", "evaluator", "summary", "screenshots", "replays",
    "intervention_applied",
    *METRICS,
)
SPLIT_NAMES = {"dev": "development", "pilot": "development", "test": "static"}
COVERAGE_STATUSES = ("valid", "excluded", "failed", "pending", "invalid")
VISUAL_TYPES = {".gif": "replay", ".mp4": "replay", ".png": "image", ".webp": "image"}


def _read_json(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def _rel(path, root):
    return Path(os.path.relpath(path, root)).as_posix()


def _write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def _write_csv(path, rows, keys):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)


def _write_application_summary(path, rows, coverage_summary, comparisons):
    """Write a concise, conservative project description for an application."""
    available = [item for item in comparisons if item.difference is not None]
    scopes = {item.split for item in available}
    first = (
        "EmbodiedMind is a self-initiated study of how local language-model agents use memory "
        "and revise beliefs while navigating partially observable, symbolic MiniGrid and BabyAI worlds. "
        "The protocol compares reactive, bounded text-history, structured-memory and belief-revision "
        "agents using a shared frozen model, controller, action budget and seeded evaluation. "
        "Only the evaluator accesses privileged simulation state. "
    )
    if {"static", "dynamic"} <= scopes:
        second = (
            f"The evidence package currently contains {coverage_summary['valid']} validated episodes "
            "across its supplied runs. Paired comparisons examine static mission success and the "
            "frequency of actions tied to contradicted evidence under custom world changes. "
        )
    else:
        second = (
            f"The evidence package currently contains {coverage_summary['valid']} validated episodes "
            "across its supplied runs. The planned paired analysis examines static mission success "
            "and actions tied to contradicted evidence under controlled custom world changes. "
        )
    failures = any(row["status"] == "valid" and not row.get("success") for row in rows)
    package = (
        "The research package preserves agent traces and reproducible figures"
        if coverage_summary["valid"] else
        "The research package documents the benchmark setup and current coverage"
    )
    end = (
        package + (", including observed task failures. " if failures else ". ") +
        "The study addresses planning in abstract simulation and uses frozen model weights throughout."
    )
    path.write_text(first + second + end + "\n", encoding="utf-8")


def _validated_trajectory(path):
    """Reject truncated and unreadable traces before a result enters the score."""
    with path.open(encoding="utf-8") as trace:
        count = 0
        for line in trace:
            if not line.strip():
                continue
            if not isinstance(json.loads(line), dict):
                raise ValueError(f"{path} contains a non-object event")
            count += 1
    if not count:
        raise ValueError(f"{path} is empty")


def _episode_id(job):
    value = str(job["id"])
    if not value or value in {".", ".."} or "/" in value or "\\" in value:
        raise ValueError(f"Unsafe episode ID {value!r}")
    return value


def _attempt_paths(run_dir, directory, job_id):
    locations = (run_dir / "attempts" / job_id, directory / "attempts")
    return [item for path in locations if path.is_dir() for item in sorted(path.iterdir()) if item.is_dir()]


def _count_attempts(attempt_paths, summary):
    reported = summary.get("attempts")
    count = len(attempt_paths) + 1
    if isinstance(reported, list):
        return max(count, len(reported))
    if isinstance(reported, int):
        return max(count, reported)
    return count


def _validate_integrity(directory, required):
    path = directory / "integrity.json"
    if not path.exists() and not required:
        return
    hashes = _read_json(path)
    if not {"summary.json", "trajectory.jsonl", "evaluator.json"} <= hashes.keys():
        raise ValueError("Integrity record is missing required episode files")
    for name, expected in hashes.items():
        artifact = Path(name)
        if (artifact.is_absolute() or ".." in artifact.parts or not isinstance(expected, str)
                or not (directory / artifact).resolve().is_relative_to(directory.resolve())):
            raise ValueError("Malformed integrity record")
        if _digest(directory / name) != expected:
            raise ValueError(f"Episode file checksum failed: {name}")


def _normalize_metrics(row, summary):
    aliases = {
        "steps": "primitive_steps",
        "calls": "llm_calls",
        "completion_tokens": "output_tokens",
        "inference_seconds": "inference_time_seconds",
        "invalid_actions": "invalid_action_count",
        "stale_actions": "stale_action_count",
        "unsupported_claims": "hallucinations",
        "post_contradiction_recovered": "recovered",
    }
    for metric in METRICS:
        value = summary.get(metric, summary.get(aliases.get(metric, "")))
        if numeric(value) is not None:
            row[metric] = value
    if "total_tokens" not in row and {"prompt_tokens", "completion_tokens"} <= row.keys():
        row["total_tokens"] = row["prompt_tokens"] + row["completion_tokens"]
    if "stale_action_rate" not in row and "stale_actions" in row and row.get("steps", 0) > 0:
        row["stale_action_rate"] = row["stale_actions"] / row["steps"]


def _artifact_list(directory, suffixes, root):
    return " | ".join(
        _rel(path, root) for path in sorted(directory.rglob("*"))
        if path.is_file() and path.suffix.lower() in suffixes
        and "attempts" not in path.relative_to(directory).parts[:-1]
    )


def _load_episode(run_dir, run_id, default_split, job, root, integrity_required):
    job_id = _episode_id(job)
    variant = str(job["variant"]).upper()
    if variant not in KNOWN_VARIANTS:
        raise ValueError(f"Unrecognized condition {variant!r} in {job_id}")
    split = str(job.get("split", default_split)).lower()
    directory = run_dir / "episodes" / job_id
    summary_path = directory / "summary.json"
    trajectory = directory / "trajectory.jsonl"
    row = {
        "run_id": run_id, "job_id": job_id, "split": SPLIT_NAMES.get(split, split),
        "environment": str(job["environment"]), "seed": int(job["seed"]),
        "mission": job.get("mission", ""), "intervention": str(job.get("intervention") or "none"),
        "variant": variant, "replicate": int(job.get("replicate", 0)), "status": "pending",
        "outcome": "", "reason": "", "attempts": 0, "trajectory": "", "evaluator": "",
        "summary": "", "screenshots": "", "replays": "",
    }
    attempts = _attempt_paths(run_dir, directory, job_id)
    row["attempts"] = len(attempts)
    if not summary_path.is_file():
        row["reason"] = ("An attempt ended before finalizing" if attempts else "Episode never started")
        errors = []
        for path in attempts:
            error_path = path / "error.json"
            if error_path.is_file():
                try:
                    errors.append(_read_json(error_path).get("error", "Unknown attempt error"))
                except (OSError, ValueError):
                    errors.append(f"Unreadable error record at {_rel(error_path, root)}")
        if errors:
            row["status"] = "failed"
            row["reason"] = str(errors[-1])
        return row
    row["summary"] = _rel(summary_path, root)
    row["attempts"] = max(1, row["attempts"])
    try:
        summary = _read_json(summary_path)
        row["attempts"] = _count_attempts(attempts, summary)
        status = str(summary.get("status", "valid")).lower()
        row["outcome"] = str(summary.get("outcome", ""))
        row["reason"] = str(summary.get("reason") or summary.get("error") or "")
        if status in {"excluded", "invalid_world"}:
            if not row["reason"]:
                raise ValueError("Excluded episode requires a reason")
            row["status"] = "excluded"
            return row
        if status in {"failed", "infra_error", "infra_failed", "error", "aborted", "infrastructure_error"}:
            row["status"] = "failed"
            return row
        if status not in {"valid", "completed", "complete", "ok", "success"}:
            raise ValueError(f"Unknown episode status {status}")
        if not isinstance(summary.get("success"), bool):
            raise ValueError("Finalized result missing boolean success")
        mission = summary.get("mission", row["mission"])
        if not isinstance(mission, str) or not mission:
            raise ValueError("Finalized result missing mission")
        if not row["outcome"]:
            raise ValueError("Finalized result missing outcome")
        for field in ("id", "environment", "variant", "seed", "intervention", "replicate"):
            if field in summary and field in job and summary[field] != job[field]:
                raise ValueError(f"Finalized result {field} disagrees with the frozen roster")
        if job.get("mission") and mission != job["mission"]:
            raise ValueError("Finalized result mission disagrees with the frozen roster")
        _validate_integrity(directory, integrity_required)
        _validated_trajectory(trajectory)
        row["mission"] = mission
        row["trajectory"] = _rel(trajectory, root)
        row["evaluator"] = " | ".join(_rel(path, root) for path in sorted(directory.glob("evaluator*")) if path.is_file())
        row["screenshots"] = _artifact_list(directory, {".png", ".webp"}, root)
        row["replays"] = _artifact_list(directory, {".gif", ".mp4"}, root)
        _normalize_metrics(row, summary)
        if isinstance(summary.get("intervention_applied"), bool):
            row["intervention_applied"] = summary["intervention_applied"]
        row["status"] = "valid"
    except (OSError, ValueError) as error:
        row["status"] = "invalid"
        row["reason"] = str(error)
    return row


def load_run(run_dir: Path, display_root: Path | None = None):
    """Load frozen roster and validated episode records."""
    run_dir = Path(run_dir).resolve()
    manifest = _read_json(run_dir / "manifest.json")
    run_id = str(manifest.get("run_id", run_dir.name))
    split = str(manifest.get("split", "unknown"))
    root = Path(display_root).resolve() if display_root else run_dir
    rows = []
    known_ids = set()
    known_cells = set()
    for job in manifest["jobs"]:
        row = _load_episode(run_dir, run_id, split, job, root, integrity_required="lock_sha256" in manifest)
        key = tuple(row[field] for field in ("split", "environment", "intervention", "seed", "variant", "replicate"))
        if row["job_id"] in known_ids or key in known_cells:
            raise ValueError(f"Duplicate roster entry {key!r} in {run_id}")
        known_ids.add(row["job_id"])
        known_cells.add(key)
        rows.append(row)
    if not rows:
        raise ValueError(f"Frozen roster for {run_id} is empty")
    return manifest, rows


def coverage(episodes):
    """Count planned cells, validated outcomes, and auditable missing data."""
    strata = []
    for (split, environment, intervention), rows in sorted(stratify(episodes).items()):
        counts = {}
        for variant in sorted({row["variant"] for row in rows}):
            variant_rows = [row for row in rows if row["variant"] == variant]
            statuses = Counter(row["status"] for row in variant_rows)
            counts[variant] = {
                "planned": len(variant_rows),
                **{status: statuses[status] for status in COVERAGE_STATUSES},
            }
            if split == "dynamic" and intervention != "none":
                scored = [row for row in variant_rows if row["status"] == "valid"]
                counts[variant].update(
                    applied=sum(row.get("intervention_applied") is True for row in scored),
                    unapplied=sum(row.get("intervention_applied") is False for row in scored),
                    exposure_unknown=sum("intervention_applied" not in row for row in scored),
                )
        valid = {
            variant: {(row["seed"], row["mission"], row["replicate"]) for row in rows
                      if row["variant"] == variant and row["status"] == "valid"}
            for variant in counts
        }
        matched = set.intersection(*valid.values())
        planned = {
            variant: {(row["seed"], row["replicate"]) for row in rows if row["variant"] == variant}
            for variant in counts
        }
        planned_match = set.intersection(*planned.values())
        strata.append({
            "split": split, "environment": environment, "intervention": intervention,
            "planned": len(rows), "planned_matched_cells": len(planned_match), "matched_cells": len(matched),
            "matched_seeds": len({seed for seed, _, _ in matched}), "variants": counts,
        })
    statuses = Counter(row["status"] for row in episodes)
    issues = [{field: row[field] for field in ("run_id", "job_id", "status", "reason", "attempts")}
              for row in episodes if row["status"] != "valid"]
    attempted = sum(row["attempts"] > 0 for row in episodes)
    return {
        "planned": len(episodes), "attempted": attempted, "unattempted": len(episodes) - attempted,
        "attempt_records": sum(row["attempts"] for row in episodes),
        **{status: statuses[status] for status in COVERAGE_STATUSES},
        "strata": strata, "nonvalid_cells": issues,
    }


def evaluate(run_dir: Path):
    """Verify roster coverage without generating figures."""
    _, rows = load_run(run_dir)
    return coverage(rows)


def _digest(path):
    with path.open("rb") as content:
        return hashlib.file_digest(content, "sha256").hexdigest()


def _kind(path):
    if path.name.startswith("evaluator"):
        return "private-evaluator"
    if path.name == "trajectory.jsonl":
        return "trajectory"
    if path.name == "manifest.json":
        return "manifest"
    return VISUAL_TYPES.get(path.suffix.lower(), path.suffix.lower().lstrip(".") or "file")


def _artifact_index(run_dirs, out, metadata):
    output = out / "artifact-index.json"
    root = out.parent
    entries = []
    seen = set()
    for tree in [*run_dirs, out]:
        for path in sorted(tree.rglob("*")):
            if (not path.is_file() or path.is_symlink()
                    or path.name in {"artifact-index.json", ".gitkeep", "supervisor.lock"} or path in seen):
                continue
            seen.add(path)
            run_id = job_id = ""
            for run_dir in run_dirs:
                if path.is_relative_to(run_dir):
                    run_id = metadata[run_dir]
                    parts = path.relative_to(run_dir).parts
                    if len(parts) >= 3 and parts[0] in {"episodes", "attempts"}:
                        job_id = parts[1]
                    break
            entries.append({
                "path": _rel(path, root), "kind": _kind(path), "size_bytes": path.stat().st_size,
                "sha256": _digest(path), "run_id": run_id, "job_id": job_id,
                "visibility": "private" if run_id and not path.is_relative_to(out) else "derived",
            })
            if run_id and len(parts) >= 4 and parts[0] == "attempts":
                entries[-1]["attempt_id"] = parts[2]
    _write_json(output, {"paths_relative_to": "..", "hash_algorithm": "sha256", "files": entries})


def _mean_display(value):
    return "—" if value is None else f"{value:.3f}"


def _means(rows, variant, metric):
    values = [value for row in rows if row["status"] == "valid" and row["variant"] == variant
              if (value := numeric(row.get(metric))) is not None]
    return _mean_display(fmean(values) if values else None)


def _comparison_table(comparisons):
    header = [
        "| Split | Environment | Intervention | Metric | Contrast | Matched seeds | Difference | 95% interval |",
        "| --- | --- | --- | --- | --- | ---: | ---: | --- |",
    ]
    records = []
    for item in comparisons:
        primary = (item.split == "static" and item.metric == "success" and item.control == "B1") or (
            item.split == "dynamic" and item.metric == "stale_action_rate" and item.control == "B2"
        )
        development_comparison = (item.split == "development" and item.treatment in
                                  {"B0G", "B3G", "B4", "B5", "B6", "B7", "B8", "B9N", "B9", "B10"} and
                                  item.metric in {"success", "blocked_actions", "verification_requests"})
        if not (primary or development_comparison):
            continue
        interval = "—"
        if item.lower_95 is not None and item.upper_95 is not None:
            interval = f"[{item.lower_95:.3f}, {item.upper_95:.3f}]"
        records.append(
            f"| {item.split} | {item.environment} | {item.intervention} | {item.metric} | "
            f"{item.treatment} − {item.control} | {item.paired_n} | {_mean_display(item.difference)} | {interval} |"
        )
    return header + records if records else ["The supplied runs contain no planned primary held-out contrasts."]


def _write_report(path, manifests, rows, summary, comparisons, plots, argv_example):
    roster = sorted({row["split"] for row in rows})
    held_out = {"static", "dynamic"}.issubset(roster)
    all_accounted_for = (summary["planned"] == summary["valid"] + summary["excluded"] and
                         all(item["matched_seeds"] > 0 for item in summary["strata"]))
    lines = [
        "# EmbodiedMind experiment report", "",
        "EmbodiedMind evaluates memory and belief revision with a frozen local language model in "
        "partially observable symbolic MiniGrid/BabyAI tasks.", "",
        f"Run scope includes {', '.join(roster)}. "
        + ("The supplied rosters are accounted for. Consult the frozen protocol and exclusion reasons for benchmark acceptance."
           if all_accounted_for else "Coverage is incomplete under the supplied rosters. See the unresolved cells in the coverage file."), "",
        f"Across these runs, {summary['attempted']} of {summary['planned']} cells were attempted, "
        f"{summary['valid']} validated, {summary['excluded']} excluded and {summary['attempt_records']} attempts recorded.",
        "", "## Coverage and descriptive results", "",
        "| Split | Environment | Intervention | Condition | Planned | Valid | Matched seeds | Success | Steps | Tokens | Applied / known exposure |",
        "| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    groups = stratify(rows)
    for item in summary["strata"]:
        key = (item["split"], item["environment"], item["intervention"])
        for variant, counts in item["variants"].items():
            means = [_means(groups[key], variant, metric) for metric in ("success", "steps", "total_tokens")]
            exposure = "—"
            if "applied" in counts:
                exposure = f"{counts['applied']} / {counts['applied'] + counts['unapplied']}"
            lines.append(
                f"| {' | '.join(key)} | {variant} | {counts['planned']} | {counts['valid']} | "
                f"{item['matched_seeds']} | {' | '.join(means)} | {exposure} |"
            )
    lines.extend(["", "## Primary paired contrasts", ""])
    lines.extend(_comparison_table(comparisons))
    lines.extend([
        "", "Differences use only identical environment, intervention, mission, seed and replicate. "
        "Replicate differences are averaged within seed before estimating intervals with a deterministic "
        "4,000-draw seed bootstrap. Intervals are shown for at least five matched seeds. "
        "Valid task failures are included. Missing measurements stay missing. The main dynamic comparisons "
        "retain episodes under their assigned condition. Exposure counts show how often the intervention was recorded as applied.",
        "", "## Interpretation and limits", "",
        "- Treat development evidence as feasibility and diagnostics. The two held-out benchmark rosters "
        + ("are represented in this report." if held_out else "must both be supplied for full experiment interpretation."),
        "- Estimates apply to the frozen local model, configured action/prompt budgets and abstract 2D worlds. "
        "The study concerns planning in simulation.",
        "- A small paired sample and sparse contradiction events can yield imprecise estimates. "
        "The stale-action measure requires an explicit evidence ID and misses uncited intent. "
        "Unsupported references are missing, invalid or unprovided IDs, a narrower observation than all model hallucinations.",
        "- B3 adds belief revision, aging warnings and working memory to structured memory. "
        "The contrast with B2 evaluates that bundle. The B1 result applies to the specified bounded factual history.",
        "- A hidden relocation can be missed when either cell is visible or a policy changes the world before the trigger. "
        "Assigned-arm results include these no-ops. Equal measured rates with rare cited contradictions give limited evidence about revision.",
        "- Traces record prompt usage, which can vary by memory treatment under a shared ceiling. "
        "Shorter paths and higher success may compete with greater inference cost.",
        "- The observation encoder and model use symbolic features. Navigation depends on the shared controller "
        "and odometry inferred from permitted action feedback. Identical-looking objects can be misidentified.",
        "", "## Failure evidence", "",
    ])
    failures = sorted(
        (row for row in rows if row["status"] == "valid" and not row.get("success")),
        key=lambda row: (row["split"], row["environment"], row["intervention"], row["variant"], row["seed"]),
    )
    selected = {}
    for row in failures:
        selected.setdefault((row["split"], row["environment"], row["intervention"]), row)
    if selected:
        for row in selected.values():
            lines.append(
                f"- {row['split']} · {row['environment']} · {row['intervention']} · "
                f"{row['variant']} seed {row['seed']} · {row['outcome']} "
                f"({row.get('steps', 'unknown')} steps). Trace at `{row['trajectory']}`."
            )
            if row["screenshots"] or row["replays"]:
                links = []
                for kind in ("screenshots", "replays"):
                    for artifact in filter(None, row[kind].split(" | ")):
                        target = "../" + artifact
                        links.append(f"[{Path(artifact).name}]({target})")
                lines.append("  - Private visual evidence: " + ", ".join(links))
    else:
        lines.append("No validated task failures were recorded in the supplied rows.")
    lines.extend(["", "## Outcome distribution", ""])
    for (split, environment, intervention), group in sorted(groups.items()):
        outcomes = Counter(row["outcome"] for row in group if row["status"] == "valid")
        if outcomes:
            detail = ", ".join(f"{outcome}: {count}" for outcome, count in sorted(outcomes.items()))
            lines.append(f"- {split} · {environment} · {intervention} — {detail}")
    if plots:
        lines.extend(["", "## Regenerable figures", ""])
        lines.extend(f"- [{plot.stem.replace('-', ' ')}]({plot.relative_to(path.parent).as_posix()})" for plot in plots)
    lines.extend(["", "## Provenance and reproduction", ""])
    for run_dir, manifest in manifests:
        lines.append(
            f"- Run `{manifest.get('run_id', run_dir.name)}`. Manifest at `{run_dir / 'manifest.json'}`. "
            f"Source `{manifest.get('git_commit', manifest.get('commit', 'see manifest'))}`."
        )
    lines.extend([
        "", f"Regenerate outputs with `{argv_example}`.", "",
        "[Episode metrics](metrics.csv) · [Paired results](comparisons.csv) · "
        "[Coverage and omissions](coverage.json) · [Evidence checksums](artifact-index.json) · "
        "[Application summary](application-summary.md)", "",
        "The evidence index may point to private raw logs, model exchanges, evaluator traces and renderings.",
        "",
    ])
    path.write_text("\n".join(lines), encoding="utf-8")


def generate_combined_report(run_dirs, output_dir: Path, argv_example: str | None = None) -> Path:
    """Generate the analysis bundle from one frozen manifest or multiple run splits."""
    from .plots import make_plots

    directories = list(dict.fromkeys(Path(run_dir).resolve() for run_dir in run_dirs))
    if not directories:
        raise ValueError("At least one run directory is required")
    output_dir = Path(output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    manifests, episodes = [], []
    for run_dir in directories:
        manifest, rows = load_run(run_dir, display_root=output_dir.parent)
        manifests.append((run_dir, manifest))
        episodes.extend(rows)
    comparisons = compare(episodes)
    summary = coverage(episodes)
    _write_csv(output_dir / "metrics.csv", episodes, EPISODE_FIELDS)
    _write_csv(output_dir / "comparisons.csv", [asdict(row) for row in comparisons], [field.name for field in fields(Comparison)])
    _write_json(output_dir / "coverage.json", summary)
    plots = make_plots(episodes, comparisons, output_dir / "figures")
    report = output_dir / "report.md"
    if argv_example is None:
        options = " ".join(f'"{directory}"' for directory in directories)
        argv_example = f'python -m embodiedmind.cli report {options} --output "{output_dir}"'
    _write_report(report, manifests, episodes, summary, comparisons, plots, argv_example)
    _write_application_summary(output_dir / "application-summary.md", episodes, summary, comparisons)
    _artifact_index(directories, output_dir, {path: str(manifest.get("run_id", path.name)) for path, manifest in manifests})
    return report


def generate_report(run_dir: Path) -> Path:
    """Generate the report inside a single run's directory."""
    run_dir = Path(run_dir).resolve()
    return generate_combined_report([run_dir], run_dir / "report")
