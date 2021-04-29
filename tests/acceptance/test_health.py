def test_should_show_application_health_status(client):
    rv = client.get("/health")

    assert rv.status_code == 200

    json_data = rv.get_json()
    assert json_data["status"] == "ok"
