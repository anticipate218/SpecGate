"""List, download, and maintain SpecGate modules."""

from __future__ import annotations

import shutil
from pathlib import Path

MODULE_DIR = Path(__file__).resolve().parent / "modules"
USER_DIR = Path.home() / ".specgate" / "modules"

CATALOG = {
    "sep": "Synonym evidence pooling (temperature soft-OR).",
    "bias_correct": "Soft-OR inflation correction.",
    "mse": "Multi-scale evidence views.",
    "tta": "Horizontal-flip aggregation.",
    "pamr": "Affinity-based mask refinement.",
}


def available_modules():
    return dict(CATALOG)


def _source(name):
    path = MODULE_DIR / f"{name}.py"
    if not path.is_file():
        raise FileNotFoundError(f"module {name!r} is not in the catalog")
    return path


def download_modules(names, dest=None):
    dest = Path(dest) if dest else USER_DIR
    dest.mkdir(parents=True, exist_ok=True)
    installed = []
    for name in names:
        if name not in CATALOG:
            raise KeyError(f"unknown module {name!r}; choose from {sorted(CATALOG)}")
        target = dest / f"{name}.py"
        shutil.copy2(_source(name), target)
        installed.append(str(target))
    return installed


def module_status(dest=None):
    dest = Path(dest) if dest else USER_DIR
    status = {}
    for name in CATALOG:
        bundled = (MODULE_DIR / f"{name}.py").is_file()
        local = (dest / f"{name}.py").is_file()
        status[name] = {
            "bundled": bundled,
            "downloaded": local,
            "path": str(dest / f"{name}.py") if local else None,
        }
    return status
