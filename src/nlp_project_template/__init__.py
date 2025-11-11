"""NLP Project Template - A template repository for NLP projects."""

from pathlib import Path


def project_root_dir() -> Path:
    """Get the project root directory."""
    return Path(__file__).parent.parent.parent
