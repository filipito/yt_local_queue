def test_list_tracks_returns_empty(client):
    response = client.get("/api/tracks")
    assert response.status_code == 200
    assert response.json() == []


def test_get_track_returns_not_found(client):
    response = client.get("/api/tracks/some-id")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "not_found"


def test_delete_track_returns_not_deleted(client):
    response = client.delete("/api/tracks/some-id")
    assert response.status_code == 200
    data = response.json()
    assert data["deleted"] is False
