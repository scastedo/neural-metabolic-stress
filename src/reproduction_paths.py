"""Portable input paths; importing this module never loads data or simulator code."""
import os
from pathlib import Path

BUNDLE_ROOT = Path(__file__).resolve().parents[1]


def _input_path(variable, default):
    value = Path(os.environ.get(variable, str(default))).expanduser()
    return value if value.is_absolute() else BUNDLE_ROOT / value


RAW_DATA_DIR = _input_path("CALCIUM_DATA_DIR", BUNDLE_ROOT / "data" / "raw")
CACHE_DIR = _input_path("CALCIUM_CACHE_DIR", BUNDLE_ROOT / "data" / "cache")
MOVIE_DATA_DIR = _input_path("CALCIUM_MOVIE_DIR", BUNDLE_ROOT / "data" / "movie")
CANN_RUNS_DIR = _input_path("CALCIUM_RUNS_DIR", BUNDLE_ROOT / "data" / "continuous_attractor")
CANN_STATIC_RUNS_DIR = _input_path("CALCIUM_STATIC_RUNS_DIR", BUNDLE_ROOT / "data" / "continuous_attractor_static")
STYLE_PATH = BUNDLE_ROOT / "styles" / "paper_style.mplstyle"

INPUT_DIRS = {
    "raw": RAW_DATA_DIR,
    "cache": CACHE_DIR,
    "movie": MOVIE_DATA_DIR,
    "runs": CANN_RUNS_DIR,
    "static_runs": CANN_STATIC_RUNS_DIR,
    "styles": STYLE_PATH.parent,
}
