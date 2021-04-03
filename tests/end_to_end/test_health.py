def test_index(client):
    rv = client.get("/health")

    assert rv.status_code == 200
    assert b'{"status":"ok"}' in rv.data
