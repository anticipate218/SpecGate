"""Turn a dataset specification into module switches.

The spatial tests use ground sampling distance and label semantics.
The score test uses a bound on soft-OR inflation. Nothing here reads a
target image or a target-domain label.
"""

import math

GSD_GATE = 0.2
SEP_TAU = 0.07


def select_modules(
    gsd,
    parcel_scale,
    bg_evaluated,
    prob_thd,
    max_synonyms,
    sep_tau=SEP_TAU,
):
    """Return which registered modules should run.

    gsd            ground sampling distance in metres
    parcel_scale   True when the labels name large contiguous parcels
    bg_evaluated   True when background enters the reported metric
    prob_thd       decision threshold used for that dataset
    max_synonyms   largest synonym count of any class
    """
    spatial = (gsd >= GSD_GATE) and bool(parcel_scale)
    inflation = sep_tau * math.log(max_synonyms) if max_synonyms > 1 else 0.0
    return {
        "sep": True,
        "tta": True,
        "mse": spatial,
        "pamr": spatial,
        "bias_correct": bool(bg_evaluated and inflation >= 0.5 * prob_thd),
    }
