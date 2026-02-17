from schemas import DownloadRequest, DownloadResponse, SearchResult, Song


def test_song_with_all_fields():
    song = Song(title="Test", artist="Artist", duration=180, genre="Rock", album="LP")
    assert song.title == "Test"
    assert song.duration == 180


def test_song_optional_fields_default_none():
    song = Song(title="Test", artist="Artist")
    assert song.duration is None
    assert song.genre is None
    assert song.album is None


def test_search_result_with_required_fields():
    result = SearchResult(video_id="abc123", title="Video", channel="Channel")
    assert result.video_id == "abc123"
    assert result.duration is None
    assert result.thumbnail_url is None


def test_download_request():
    req = DownloadRequest(video_id="abc123")
    assert req.video_id == "abc123"
    assert req.title is None


def test_download_response_success():
    resp = DownloadResponse(
        status="success",
        video_id="abc123",
        title="Song",
        file_path="/tmp/abc123.mp3",
    )
    assert resp.status == "success"
    assert resp.error is None


def test_download_response_error():
    resp = DownloadResponse(
        status="error",
        video_id="abc123",
        error="Download failed",
    )
    assert resp.status == "error"
    assert resp.error == "Download failed"
