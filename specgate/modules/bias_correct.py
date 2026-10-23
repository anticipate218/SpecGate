"""Subtract the worst-case soft-OR inflation from a pooled score."""

from specgate.modules.sep import inflation_bound, lse


def correct(values, tau=0.07):
    """Return LSE(values) - tau * ln(k). Never exceeds the hard maximum."""
    k = len(values)
    return lse(values, tau=tau) - inflation_bound(k, tau=tau)
