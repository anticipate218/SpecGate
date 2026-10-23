"""SpecGate: specification-guided modular inference."""

from specgate.scheduler import select_modules
from specgate.registry import available_modules, download_modules, module_status

__version__ = "0.1.0"
__all__ = [
    "select_modules",
    "available_modules",
    "download_modules",
    "module_status",
]
