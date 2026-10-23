"""Synonym evidence pooling by a temperature soft-OR."""

import math


def lse(values, tau=0.07):
    """Log-sum-exp over synonym scores. A single value is returned unchanged."""
    if not values:
        raise ValueError("values must be non-empty")
    if len(values) == 1:
        return values[0]
    m = max(values)
    acc = 0.0
    for v in values:
        acc += math.exp((v - m) / tau)
    return m + tau * math.log(acc)


def inflation_bound(k, tau=0.07):
    """Worst-case soft-OR offset: tau * ln(k)."""
    if k <= 1:
        return 0.0
    return tau * math.log(k)
