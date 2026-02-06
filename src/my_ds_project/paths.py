from __future__ import annotations
from pathlib import Path

MARKER = ".project-root"

def find_project_root(start: Path | None = None) -> Path:
    here = (start or Path.cwd()).resolve()
    for p in [here, *here.parents]:
        if (p / MARKER).exists():
            return p
    raise RuntimeError(f"Could not find project root starting from {here}")

PROJECT_ROOT = find_project_root()

DATA_DIR = PROJECT_ROOT / "data"
DATA_RAW = DATA_DIR / "raw"
DATA_INTERIM = DATA_DIR / "interim"
DATA_PROCESSED = DATA_DIR / "processed"

REPORTS_DIR = PROJECT_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"