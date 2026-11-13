"""Generate headless figures from the same normalized rows as the report."""

from pathlib import Path
from statistics import fmean

import matplotlib

matplotlib.use("Agg")

from matplotlib import pyplot as plt

from .statistics import numeric, stratify


COLORS = {"B0": "#64748b", "B1": "#31736b", "B2": "#b47035", "B3": "#344e90"}
PLOT_GROUPS = {
    "success": (("success", "Mission success", "Share of episodes"),),
    "efficiency": (
        ("steps", "Primitive steps", "Steps per episode"),
        ("calls", "Model calls", "Calls per episode"),
        ("total_tokens", "Prompt and completion tokens", "Tokens per episode"),
        ("inference_seconds", "Inference time", "Seconds per episode"),
    ),
    "belief": (
        ("stale_action_rate", "Actions based on contradicted evidence", "Share of actions"),
        ("unsupported_claims", "Unsupported evidence references", "Count per episode"),
        ("post_contradiction_recovered", "Recovery after contradiction", "Share of eligible episodes"),
        ("steps_to_recovery", "Steps to recovery", "Steps among recovered episodes"),
    ),
}


def _save(fig, path: Path):
    fig.tight_layout(pad=1.3)
    fig.savefig(path, dpi=170, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def make_plots(episodes, comparisons, destination: Path) -> list[Path]:
    destination.mkdir(parents=True, exist_ok=True)
    plots = []
    strata = sorted(stratify(episodes).items())
    for name, definitions in PLOT_GROUPS.items():
        available = [
            (metric, title, units) for metric, title, units in definitions
            if any(numeric(episode.get(metric)) is not None for episode in episodes if episode["status"] == "valid")
        ]
        if not available:
            continue
        fig, axes = plt.subplots(len(available), 1, figsize=(max(8, len(strata) * 2.1), len(available) * 3.35), squeeze=False)
        variants = sorted({episode["variant"] for episode in episodes})
        width = 0.79 / len(variants)
        for ax, (metric, title, units) in zip(axes[:, 0], available):
            for index, variant in enumerate(variants):
                xs, means, counts = [], [], []
                for place, (_, group) in enumerate(strata):
                    values = [
                        value for row in group if row["variant"] == variant and row["status"] == "valid"
                        if (value := numeric(row.get(metric))) is not None
                    ]
                    if values:
                        xs.append(place + (index - (len(variants) - 1) / 2) * width)
                        means.append(fmean(values))
                        counts.append(len(values))
                bars = ax.bar(xs, means, width, label=variant, color=COLORS.get(variant))
                ax.bar_label(bars, labels=[f"n={count}" for count in counts], padding=3, fontsize=7)
            ax.set_title(title, loc="left", weight="bold")
            ax.set_ylabel(units)
            ax.set_xticks(range(len(strata)), [f"{split} · {intervention}\n{env}" for (split, env, intervention), _ in strata], fontsize=8)
            ax.grid(axis="y", alpha=0.2)
            ax.set_axisbelow(True)
            ax.margins(y=0.22)
            if metric in {"success", "stale_action_rate", "post_contradiction_recovered"}:
                ax.set_ylim(0, 1.15)
        axes[0, 0].legend(loc="upper right", ncols=max(1, len(variants)), frameon=False)
        path = destination / f"{name}.png"
        _save(fig, path)
        plots.append(path)

    selected = [
        result for result in comparisons if result.difference is not None
        and (result.metric == "success" or (result.metric == "stale_action_rate" and result.control == "B2"))
    ]
    if selected:
        fig, ax = plt.subplots(figsize=(10, max(2.7, 0.46 * len(selected) + 1)))
        for index, result in enumerate(selected):
            point = result.difference
            if result.lower_95 is not None and result.upper_95 is not None:
                ax.hlines(index, result.lower_95, result.upper_95, color=COLORS[result.treatment], linewidth=1.5)
            ax.scatter([point], [index], color=COLORS[result.treatment], zorder=3)
        ax.set_yticks(range(len(selected)), [
            f"{result.split} · {result.environment} · {result.intervention} · {result.metric}\n"
            f"{result.treatment} − {result.control} (matched n={result.paired_n})" for result in selected
        ], fontsize=8)
        ax.axvline(0, color="#505050", linewidth=0.8, linestyle="--")
        ax.invert_yaxis()
        ax.set_xlabel("Paired difference (95% bootstrap interval when estimable)")
        path = destination / "paired-comparisons.png"
        _save(fig, path)
        plots.append(path)
    return plots
