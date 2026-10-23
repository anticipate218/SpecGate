"""Build content-scale views without changing the backbone input size."""


def content_scales(native=1024, extras=(640,)):
    """Return the long-side sizes used for multi-scale evidence."""
    scales = [native]
    for s in extras:
        if 0 < s < native:
            scales.append(s)
    return scales
