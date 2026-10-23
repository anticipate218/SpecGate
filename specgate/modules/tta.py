"""Horizontal-flip test-time aggregation."""


def aggregate(scores, how="mean"):
    """Reduce a list of aligned score maps.

    `scores` is a sequence of objects that support + and scalar divide,
    or plain numbers. The default is the mean, which does not inflate
    the score scale.
    """
    if not scores:
        raise ValueError("scores must be non-empty")
    if how == "max":
        out = scores[0]
        for s in scores[1:]:
            out = _pairwise_max(out, s)
        return out
    total = scores[0]
    for s in scores[1:]:
        total = total + s
    return total / float(len(scores))


def _pairwise_max(a, b):
    if hasattr(a, "maximum"):
        return a.maximum(b)
    try:
        import torch

        if torch.is_tensor(a):
            return torch.maximum(a, b)
    except ImportError:
        pass
    return a if a >= b else b
