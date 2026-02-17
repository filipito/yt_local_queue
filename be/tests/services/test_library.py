from services.library import delete_track, get_track, list_tracks, save_track


async def test_list_tracks_returns_empty():
    result = await list_tracks()
    assert result == []


async def test_get_track_returns_none():
    result = await get_track("any-id")
    assert result is None


async def test_delete_track_returns_false():
    result = await delete_track("any-id")
    assert result is False


async def test_save_track_returns_empty_string():
    result = await save_track({"title": "Test"}, "/tmp/test.mp3")
    assert result == ""
