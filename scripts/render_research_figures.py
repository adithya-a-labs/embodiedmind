"""Build documentation figures from saved reports and one evaluator replay."""
import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path
from statistics import median

import matplotlib

matplotlib.use("Agg")
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Patch
import numpy as np


B11_STAMP = "20261116-181345"
LEGACY_STUDY = "embodiedmind-20261114-0428-ist"
SHIFT = "EmbodiedMind-GoToShift-v0"
VARIANTS = "B0 B0G B1 B2 B3 B3G B4 B5 B6 B7 B8 B9N B9 B10 B11".split()
MECHANISMS = "B11T B11P B11R B11PA B11 B11C".split()
TEAL, BLUE, GOLD, GREY = "#14776e", "#345b94", "#a85f29", "#c6d0da"
HEAT = LinearSegmentedColormap.from_list("success", ["#eff4f7", "#a1cecc", "#126258"])


def read_csv(path):
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def save(fig, destination, name):
    fig.savefig(destination / f"{name}.png", dpi=170, facecolor="white")
    plt.close(fig)


def save_coverage(outputs, legacy, destination):
    rows = []
    development = []
    for table in sorted(outputs.glob("*/report/metrics.csv")):
        if table.parents[1].name.startswith("b11-combined-"):
            continue  # Its five component reports are already in this inventory.
        data = read_csv(table)
        counts = Counter(row["status"] for row in data)
        run = table.parents[1].name
        label = re.sub(r"-20\d{6}(?:[-T].*)?$", "", run)
        group = "B11 campaign" if run.startswith("b11-") else "Other saved runs"
        rows.append((label, counts["valid"], len(data), group))
        add_development(development, label, data)

    if legacy is not None:
        study = legacy / LEGACY_STUDY
        reports = read_csv(study / "final-report/metrics.csv") + read_csv(study / "pilot-report/metrics.csv")
        indexed = {}
        for row in reports:
            key = row["run_id"], row["job_id"]
            indexed[key] = row
        for table in sorted((*study.glob("*/heartbeat.json"), *legacy.glob("*/heartbeat.json"))):
            label = table.parent.name
            heartbeat = read_json(table)
            data = [row for (run, _), row in indexed.items() if run == label]
            if data:
                rows.append((label, sum(row["status"] == "valid" for row in data),
                             len(data), "Original study reports"))
                add_development(development, label, data)
            else:
                rows.append((label, heartbeat["completed"], heartbeat["planned"], "Legacy heartbeat"))

    groups = ("Original study reports", "B11 campaign", "Other saved runs", "Legacy heartbeat")
    colours = dict(zip(groups, (BLUE, TEAL, "#69618f", GOLD)))
    rows.sort(key=lambda row: (groups.index(row[3]), row[0]))
    fig, ax = plt.subplots(figsize=(10, max(5, len(rows) * 0.28 + 1.75)), layout="constrained")
    for i, (name, complete, planned, group) in enumerate(rows):
        ax.barh(i, planned, color="#e4e9ee", height=0.62)
        ax.barh(i, complete, color=colours[group], height=0.62)
        ax.annotate(f"{complete:,} / {planned:,}", (planned, i),
                    xytext=(5, 0), textcoords="offset points", va="center", fontsize=8)
    ax.set(
        yticks=range(len(rows)), yticklabels=[row[0] for row in rows],
        xlabel="Episode count (nonlinear scale)",
        title="Archive coverage and remaining roster entries",
    )
    ax.set_xscale("symlog", linthresh=1)
    ax.set_xlim(0, max(row[2] for row in rows) * 3.4)
    ax.invert_yaxis()
    handles = [Patch(facecolor=colour, label=group) for group, colour in colours.items()
               if any(row[3] == group for row in rows)]
    handles.append(Patch(facecolor="#e4e9ee", label="Remaining roster entries"))
    ax.legend(handles=handles, loc="lower right", frameon=False)
    save(fig, destination, "run-coverage")
    return rows, development


def add_development(series, label, data):
    valid = [r for r in data if r["status"] == "valid" and r["split"] in {"development", "feasibility"}]
    if valid:
        tokens = [int(row["total_tokens"]) for row in valid if row["total_tokens"]]
        series.append((label, sum(r["success"].lower() == "true" for r in valid), len(valid),
                       median(tokens) if tokens else None))


def plot_development(rows, destination):
    rows.sort(key=lambda row: row[0])
    labels = [row[0] for row in rows]
    y = range(len(rows))
    fig, (success, cost) = plt.subplots(1, 2, sharey=True, figsize=(10.2, len(rows) * 0.32 + 1.5),
                                       layout="constrained")
    proportions = [wins / n for _, wins, n, _ in rows]
    success.scatter(proportions, y, color=TEAL, s=30)
    for i, ((_, wins, n, tokens), proportion) in enumerate(zip(rows, proportions)):
        success.annotate(f"{wins}/{n}", (proportion, i), xytext=(6, 0), textcoords="offset points",
                         va="center", fontsize=8)
        if tokens is not None:
            cost.scatter(tokens / 1000, i, color=BLUE, s=30)
    success.set(xlim=(-0.04, 1.17), xlabel="Success proportion", yticks=y, yticklabels=labels)
    cost.set(xlabel="Median tokens per episode (thousands)", xlim=(-0.7, None))
    success.invert_yaxis()
    for ax in (success, cost):
        ax.grid(axis="x", alpha=0.2)
    fig.suptitle("Development and feasibility runs · within-archive summaries")
    save(fig, destination, "development-runs")


def task_name(environment, intervention):
    if environment == SHIFT:
        return "GoToShift · " + intervention.replace("_", " ")
    return re.sub(r"-v\d+$", "", re.sub(r"^(MiniGrid|BabyAI)-", "", environment))


def success_matrix(rows, variants, cases, destination, name, title):
    counts = Counter()
    wins = Counter()
    for row in rows:
        if row["status"] == "valid" and row["success"].lower() in {"true", "false"}:
            key = row["split"], row["environment"], row["intervention"], row["variant"]
            counts[key] += 1
            wins[key] += row["success"].lower() == "true"
    rates = np.full((len(cases), len(variants)), np.nan)
    fig, ax = plt.subplots(figsize=(max(8, len(variants) * 0.73), len(cases) * 0.42 + 1.8),
                           layout="constrained")
    labels = []
    for i, case in enumerate(cases):
        split, environment, intervention = case
        label = task_name(environment, intervention)
        if split == "b11-multiroom-80":
            label += " · 80 actions"
        elif label.startswith("MultiRoom"):
            label += " · 48 actions"
        labels.append(label)
        for j, variant in enumerate(variants):
            key = (*case, variant)
            n = counts[key]
            if n:
                rates[i, j] = wins[key] / n
                ax.text(j, i, f"{wins[key]}/{n}", ha="center", va="center", fontsize=8,
                        color="white" if rates[i, j] > 0.72 else "#132d3d")
            else:
                ax.text(j, i, "–", ha="center", va="center", color="#626e7b")
    im = ax.imshow(rates, aspect="auto", cmap=HEAT.with_extremes(bad="#f0f1f4"), vmin=0, vmax=1)
    ax.set(xticks=range(len(variants)), xticklabels=variants, yticks=range(len(cases)),
           yticklabels=labels, title=title)
    ax.tick_params(length=0)
    fig.colorbar(im, ax=ax, label="Success proportion", fraction=0.04, pad=0.025)
    save(fig, destination, name)


def case_groups(rows, splits):
    return sorted({(r["split"], r["environment"], r["intervention"]) for r in rows if r["split"] in splits})


def plot_paired_success(comparisons, original, destination):
    selected = []
    if original:
        selected.extend(r for r in original if r["split"] == "static" and r["metric"] == "success"
                        and (r["treatment"], r["control"]) == ("B3", "B1"))
    contrasts = {("B11P", "B11T"), ("B11R", "B11T"), ("B11R", "B11P"),
                 ("B11", "B11R"), ("B11", "B11PA"), ("B11", "B11C")}
    for row in comparisons:
        pair = row["treatment"], row["control"]
        if row["split"] != "b11-mechanisms" or row["metric"] != "success" or pair not in contrasts:
            continue
        if pair in {("B11R", "B11P"), ("B11", "B11PA")} and row["intervention"] != "relocation":
            continue
        if pair in {("B11P", "B11T"), ("B11R", "B11T")} and row["environment"] == SHIFT:
            continue
        selected.append(row)
    fig, ax = plt.subplots(figsize=(10, max(4, 0.34 * len(selected) + 1.5)), layout="constrained")
    labels = []
    for i, row in enumerate(selected):
        name = task_name(row["environment"], row["intervention"])
        labels.append(f"{name}  ·  {row['treatment']} − {row['control']}  (n={row['paired_n']})")
        effect, lower, upper = [100 * float(row[key]) for key in ("difference", "lower_95", "upper_95")]
        color = BLUE if row["split"] == "static" else TEAL
        ax.hlines(i, lower, upper, color=color, lw=2)
        ax.scatter(effect, i, color=color, zorder=3, s=22)
    ax.axvline(0, color="#667884", lw=1, ls="--")
    ax.set(yticks=range(len(labels)), yticklabels=labels,
           xlabel="Paired difference in mission success (percentage points)",
           title="Selected registered success contrasts · 95% paired bootstrap intervals")
    ax.grid(axis="x", alpha=0.18)
    ax.invert_yaxis()
    save(fig, destination, "paired-success")


def plot_controller_cost(comparisons, destination):
    rows = [r for r in comparisons if r["split"] == "b11-mechanisms"
            and (r["treatment"], r["control"]) == ("B11", "B11C")]
    metrics = [("calls", "Model calls", 1), ("total_tokens", "Tokens (thousands)", 1000),
               ("episode_wall_seconds", "Wall time (seconds)", 1)]
    cases = [(r["environment"], r["intervention"]) for r in rows if r["metric"] == "success"]
    lookup = {(r["environment"], r["intervention"], r["metric"]): r for r in rows}
    fig, axes = plt.subplots(1, 3, sharey=True, figsize=(11, 3.65), layout="constrained")
    for ax, (metric, label, scale) in zip(axes, metrics):
        for i, case in enumerate(cases):
            row = lookup[(*case, metric)]
            effect, lower, upper = [float(row[key]) / scale for key in ("difference", "lower_95", "upper_95")]
            ax.hlines(i, lower, upper, color=TEAL, lw=2)
            ax.scatter(effect, i, color=TEAL, s=28, zorder=3)
        ax.axvline(0, color="#667884", ls="--", lw=1)
        ax.set_xlabel(label)
        ax.grid(axis="x", alpha=0.18)
    axes[0].set_yticks(range(len(cases)), [task_name(*case) for case in cases])
    axes[0].invert_yaxis()
    fig.suptitle("Incremental inference cost of B11 over B11C · 30 matched seeds per condition")
    save(fig, destination, "controller-cost")


def plot_relocation(outputs, destination):
    run = outputs / f"b11-rq-shift-{B11_STAMP}" / "episodes"
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.65), layout="constrained")
    for ax, variant, color in zip(axes, ("B11P", "B11R"), (GOLD, TEAL)):
        episode = run / f"e00-s11101-relocation-{variant}-r0"
        with (episode / "evaluator-steps.jsonl").open(encoding="utf-8") as stream:
            trace = [json.loads(line) for line in stream]
        summary = read_json(episode / "summary.json")
        board = trace[0]["board"]
        event = next(event for step in trace for event in step["interventions"]
                     if event["intervention"] == "relocation" and event["applied"])
        walls = [(o["x"], o["y"]) for o in board["objects"] if o["object"] == "wall"]
        route = [(step["board"]["agent"]["x"], step["board"]["agent"]["y"]) for step in trace]
        ax.scatter(*zip(*walls), marker="s", s=145, color="#dae2e9", label="Wall")
        ax.plot(*zip(*route), color=color, lw=2, alpha=0.9, label="Agent route")
        ax.scatter(*route[0], marker="o", facecolor="white", edgecolor=color, zorder=3, label="Start")
        ax.scatter(*route[-1], marker="s", c=color, zorder=3, label="End")
        ax.scatter(*event["old_position"], marker="x", c="#7c8998", zorder=4, label="Original target")
        ax.scatter(*event["new_position"], marker="*", c="#0c4938", s=95, zorder=4, label="Relocated target")
        status = "success" if summary["success"] else summary["outcome"].replace("_", " ")
        ax.set(xlim=(-0.65, board["width"] - 0.35), ylim=(board["height"] - 0.35, -0.65),
               xticks=[], yticks=[], aspect="equal", title=f"{variant} · {status} · {summary['steps']} actions")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles[1:], labels[1:], loc="outside lower center", ncols=5, frameon=False, fontsize=9)
    fig.suptitle("GoToShift relocation · seed 11101 · evaluator coordinates")
    save(fig, destination, "relocation-trajectories")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--outputs", type=Path, default=Path("outputs"))
    parser.add_argument("--legacy-runs", type=Path, help="Optional local results/runs directory")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.size": 10, "axes.titleweight": "bold", "axes.spines.top": False,
                         "axes.spines.right": False, "axes.edgecolor": "#a8b6c2"})
    report = args.outputs / f"b11-combined-{B11_STAMP}" / "report"
    metrics = read_csv(report / "metrics.csv")
    comparisons = read_csv(report / "comparisons.csv")
    keys = {(r["run_id"], r["job_id"]) for r in metrics}
    if len(keys) != len(metrics):
        raise ValueError("The B11 combined report contains duplicate episode keys")
    original = (read_csv(args.legacy_runs / LEGACY_STUDY / "final-report/comparisons.csv")
                if args.legacy_runs is not None else [])
    coverage, development = save_coverage(args.outputs, args.legacy_runs, args.output)
    plot_development(development, args.output)
    success_matrix(metrics, VARIANTS, case_groups(metrics, {"b11-broad", "b11-multiroom-80"}),
                   args.output, "b11-benchmark", "B11 campaign · broad policy benchmark")
    success_matrix(metrics, MECHANISMS, case_groups(metrics, {"b11-mechanisms"}),
                   args.output, "b11-mechanisms", "B11 campaign · registered mechanism rosters")
    plot_paired_success(comparisons, original, args.output)
    plot_controller_cost(comparisons, args.output)
    plot_relocation(args.outputs, args.output)
    print(f"Rendered seven figures from {len(coverage)} run archives and {len(metrics)} B11 episodes.\nDevelopment metrics covered {sum(row[2] for row in development)} episodes.")


if __name__ == "__main__":
    main()
