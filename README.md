<p align="center">
  <img src="assets/banner.svg" alt="SpecGate" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-under%20review-d97706?style=for-the-badge" alt="Under review">
  <img src="https://img.shields.io/badge/python-3.9+-0f766e?style=for-the-badge" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-1d4ed8?style=for-the-badge" alt="MIT">
  <img src="https://img.shields.io/badge/modules-5-ea580c?style=for-the-badge" alt="5 modules">
</p>

<p align="center">
  Specification-guided modular inference for training-free<br>
  open-vocabulary remote sensing segmentation.
</p>

**Status: Under review.**

This repository is a small module registry, not a full evaluation dump. SpecGate keeps a frozen backbone unchanged and decides, before any target image is processed, which post-hoc operators should run. The operators can be listed, downloaded, and maintained independently of the scheduler.

## Install

```bash
git clone https://github.com/anticipate218/SpecGate.git
cd SpecGate
pip install -e .
```

## Modules

<p>
  <img src="https://img.shields.io/badge/sep-amber-f4c95d?style=flat-square&labelColor=1b2a24" alt="sep">
  <img src="https://img.shields.io/badge/bias__correct-teal-14b8a6?style=flat-square&labelColor=12352e" alt="bias_correct">
  <img src="https://img.shields.io/badge/mse-blue-3b82f6?style=flat-square&labelColor=10243d" alt="mse">
  <img src="https://img.shields.io/badge/tta-coral-f28444?style=flat-square&labelColor=2a1208" alt="tta">
  <img src="https://img.shields.io/badge/pamr-violet-c4b5fd?style=flat-square&labelColor=2d1848" alt="pamr">
</p>

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
