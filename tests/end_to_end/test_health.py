def test_index(client):
    rv = client.get("/health")

    assert rv.status_code == 200

    json_data = rv.get_json()
    assert json_data["status"] == "ok"
