def test_health_check(client):
    response = client.get("/health/health-check")
    assert response.status_code == 200
    assert response.json() == {"message": "it's alive!"}
