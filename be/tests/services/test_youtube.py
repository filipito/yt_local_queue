from unittest.mock import MagicMock, patch

from services.youtube import _download_sync, _search_sync


def test_search_sync_returns_videos():
    mock_ydl_instance = MagicMock()
    mock_ydl_instance.extract_info.return_value = {
        "entries": [
            {
                "id": "abc123",
                "title": "Test",
                "channel": "Chan",
                "duration": 120,
                "thumbnail": "http://example.com/t.jpg",
            }
        ]
    }
    mock_ydl_instance.__enter__ = MagicMock(return_value=mock_ydl_instance)
    mock_ydl_instance.__exit__ = MagicMock(return_value=False)

    with patch("services.youtube.yt_dlp.YoutubeDL", return_value=mock_ydl_instance):
        results = _search_sync("test query")
        assert len(results) == 1
        assert results[0]["video_id"] == "abc123"
        assert results[0]["title"] == "Test"


def test_search_sync_returns_empty_on_no_entries():
    mock_ydl_instance = MagicMock()
    mock_ydl_instance.extract_info.return_value = None
    mock_ydl_instance.__enter__ = MagicMock(return_value=mock_ydl_instance)
    mock_ydl_instance.__exit__ = MagicMock(return_value=False)

    with patch("services.youtube.yt_dlp.YoutubeDL", return_value=mock_ydl_instance):
        results = _search_sync("nothing")
        assert results == []


def test_download_sync_returns_metadata(tmp_path):
    mock_ydl_instance = MagicMock()
    mock_ydl_instance.extract_info.return_value = {
        "id": "abc123",
        "title": "Song Title",
        "channel": "Artist Name",
        "duration": 200,
        "ext": "mp3",
    }
    mock_ydl_instance.__enter__ = MagicMock(return_value=mock_ydl_instance)
    mock_ydl_instance.__exit__ = MagicMock(return_value=False)

    with patch("services.youtube.yt_dlp.YoutubeDL", return_value=mock_ydl_instance):
        result = _download_sync("abc123", str(tmp_path))
        assert result is not None
        assert result["video_id"] == "abc123"
        assert result["title"] == "Song Title"
        assert result["artist"] == "Artist Name"


def test_download_sync_returns_none_on_no_info(tmp_path):
    mock_ydl_instance = MagicMock()
    mock_ydl_instance.extract_info.return_value = None
    mock_ydl_instance.__enter__ = MagicMock(return_value=mock_ydl_instance)
    mock_ydl_instance.__exit__ = MagicMock(return_value=False)

    with patch("services.youtube.yt_dlp.YoutubeDL", return_value=mock_ydl_instance):
        result = _download_sync("abc123", str(tmp_path))
        assert result is None
