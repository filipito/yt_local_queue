from config import CORS_ORIGINS, PROJECT_ROOT, STORAGE_PATH, TRACKS_PATH


def test_project_root_is_directory():
    assert PROJECT_ROOT.is_dir()


def test_storage_path_under_project_root():
    assert str(STORAGE_PATH).startswith(str(PROJECT_ROOT))


def test_tracks_path_under_storage():
    assert str(TRACKS_PATH).startswith(str(STORAGE_PATH))


def test_cors_origins_non_empty():
    assert len(CORS_ORIGINS) > 0
