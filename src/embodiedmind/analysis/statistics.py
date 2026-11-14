"""Deterministic, matched analysis of completed experiment episodes."""

from collections import defaultdict
from dataclasses import dataclass
from math import isfinite
from random import Random
from statistics import fmean


METRICS = (
    "success",
    "steps",
    "calls",
    "prompt_tokens",
    "completion_tokens",
    "total_tokens",
    "inference_seconds",
    "invalid_actions",
    "stale_actions",
    "stale_action_rate",
    "unsupported_claims",
    "post_contradiction_recovered",
    "steps_to_recovery",
)


@dataclass(frozen=True)
class Comparison:
    split: str
    environment: str
    intervention: str
    metric: str
    treatment: str
    control: str
    treatment_n: int
    control_n: int
    paired_n: int
    treatment_mean: float | None
    control_mean: float | None
    difference: float | None
    lower_95: float | None
    upper_95: float | None


def numeric(value):
    """Return an observed finite metric, preserving missing values."""
    if isinstance(value, (int, float)) and isfinite(value):
        return float(value)
    return None


def stratify(episodes):
    strata = defaultdict(list)
    for episode in episodes:
        key = (episode["split"], episode["environment"], episode["intervention"])
        strata[key].append(episode)
    return strata


def _interval(differences: list[float], draws: int = 4000):
    if len(differences) < 5:
        return None, None
    rng = Random(1729)
    choices = rng.choices
    count = len(differences)
    means = sorted(fmean(choices(differences, k=count)) for _ in range(draws))
    return means[int(0.025 * (draws - 1))], means[int(0.975 * (draws - 1))]


def _variant_series(episodes, variant, metric):
    # Average genuine repeats within each seed before resampling seeds.
    reps = defaultdict(dict)
    for episode in episodes:
        if episode["variant"] != variant or episode["status"] != "valid":
            continue
        value = numeric(episode.get(metric))
        if value is None:
            continue
        key = (episode["seed"], episode["mission"])
        replicate = episode["replicate"]
        if replicate in reps[key]:
            raise ValueError(f"duplicate metric for {variant}, {key}, replicate {replicate}")
        reps[key][replicate] = value
    return reps


def compare(episodes, draws: int = 4000):
    """Compare B3 against B1/B2 using only matched seed, mission and replicate."""
    results = []
    for (split, environment, intervention), group in sorted(stratify(episodes).items()):
        variants = {episode["variant"] for episode in group}
        for control in sorted(variants.intersection({"B1", "B2"})):
            if "B3" not in variants:
                continue
            for metric in METRICS:
                treated = _variant_series(group, "B3", metric)
                baseline = _variant_series(group, control, metric)
                matches = []
                for key in sorted(treated.keys() & baseline.keys()):
                    common = sorted(treated[key].keys() & baseline[key].keys())
                    if common:
                        matches.append((
                            fmean(treated[key][repeat] for repeat in common),
                            fmean(baseline[key][repeat] for repeat in common),
                        ))
                diffs = [left - right for left, right in matches]
                low, high = _interval(diffs, draws)
                results.append(Comparison(
                    split, environment, intervention, metric, "B3", control,
                    len(treated), len(baseline), len(matches),
                    fmean(left for left, _ in matches) if matches else None,
                    fmean(right for _, right in matches) if matches else None,
                    fmean(diffs) if diffs else None, low, high,
                ))
    return results
