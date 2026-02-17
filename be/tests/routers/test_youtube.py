from unittest.mock import AsyncMock, patch


def test_search_returns_results(client):
    mock_results = [
        {
            "video_id": "abc123",
            "title": "Test Video",
            "channel": "Test Channel",
            "duration": 200,
            "thumbnail_url": "http://example.com/thumb.jpg",
        }
    ]
    with patch(
        "routers.youtube.youtube_service.search_videos",
        new_callable=AsyncMock,
        return_value=mock_results,
    ):
        response = client.get("/api/youtube-search?query=test")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["video_id"] == "abc123"


def test_search_returns_empty(client):
    with patch(
        "routers.youtube.youtube_service.search_videos",
        new_callable=AsyncMock,
        return_value=[],
    ):
        response = client.get("/api/youtube-search?query=nothing")
        assert response.status_code == 200
        assert response.json() == []


def test_search_missing_query_returns_422(client):
    response = client.get("/api/youtube-search")
    assert response.status_code == 422


def test_download_success(client):
    mock_result = {
        "video_id": "abc123",
        "title": "Song",
        "artist": "Artist",
        "duration": 180,
        "file_path": "/tmp/abc123.mp3",
    }
    with patch(
        "routers.youtube.youtube_service.download_audio",
        new_callable=AsyncMock,
        return_value=mock_result,
    ):
        response = client.post("/api/youtube-download", json={"video_id": "abc123"})
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["title"] == "Song"


def test_download_failure_returns_error(client):
    with patch(
        "routers.youtube.youtube_service.download_audio",
        new_callable=AsyncMock,
        return_value=None,
    ):
        response = client.post("/api/youtube-download", json={"video_id": "bad_id"})
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "error"
        assert data["error"] == "Download failed"
