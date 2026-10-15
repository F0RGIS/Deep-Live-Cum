"""Shared path constants for the Deep-Live-Cam project."""

import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _models_dir() -> str:
    """Prefer a writable location on Android; otherwise the repo models/ folder."""
    if sys.platform == "android" or "android" in sys.platform.lower():
        # Android app storage is writable; assets are read-only.
        base = os.environ.get("ANDROID_PRIVATE", os.path.expanduser("~"))
        return os.path.join(base, "models")
    return os.path.join(ROOT_DIR, "models")


MODELS_DIR = _models_dir()
