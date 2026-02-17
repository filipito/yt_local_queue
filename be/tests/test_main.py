def test_health_check(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "Flipi"}


def test_cors_headers_for_allowed_origin(client):
    response = client.options(
        "/",
        headers={
            "Origin": "http://localhost:3000",
            "Access-Control-Request-Method": "GET",
        },
    )
    assert response.headers["access-control-allow-origin"] == "http://localhost:3000"
