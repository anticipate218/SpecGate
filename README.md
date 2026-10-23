# SpecGate

Specification-guided modular inference for training-free open-vocabulary remote sensing segmentation.

**Status: Under review.**

This repository is a small module registry, not a full evaluation dump. SpecGate keeps a frozen backbone unchanged and decides, before any target image is processed, which post-hoc operators should run. The operators can be listed, downloaded, and maintained independently of the scheduler.

## Install

```bash
git clone https://github.com/anticipate218/SpecGate.git
cd SpecGate
pip install -e .
```

## Modules

| ID | Role |
|---|---|
| `sep` | Synonym evidence pooling (temperature soft-OR) |
| `bias_correct` | Soft-OR inflation correction |
| `mse` | Multi-scale evidence views |
| `tta` | Horizontal-flip aggregation |
| `pamr` | Affinity-based mask refinement |

```bash
python -m specgate list
python -m specgate download sep pamr
python -m specgate status
```

`download` fetches a module into `~/.specgate/modules` so it can be updated without replacing the scheduler.

## Select modules from a specification

```python
from specgate import select_modules

cfg = select_modules(
    gsd=0.30,
    parcel_scale=True,
    bg_evaluated=False,
    prob_thd=0.5,
    max_synonyms=3,
)
# {'sep': True, 'tta': True, 'mse': True, 'pamr': True, 'bias_correct': False}
```

The spatial switch uses ground sampling distance and whether the labels are parcel-scale. The score switch uses the background-scoring rule and a bound on soft-OR inflation. No target-domain label enters the decision.

## Citation

The manuscript is under review. A bibliographic entry will be added after the review process.
