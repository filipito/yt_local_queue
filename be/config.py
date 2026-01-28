"""Application configuration settings."""

from pathlib import Path

# Project root (parent of be/)
PROJECT_ROOT = Path(__file__).parent.parent

# CORS origins allowed to access the API
CORS_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3000/",
]

# Storage paths (in repository root)
STORAGE_PATH = PROJECT_ROOT / "storage"
TRACKS_PATH = STORAGE_PATH / "tracks"

# Database configuration
DATABASE_URL = f"sqlite:///{STORAGE_PATH / 'music.db'}"
