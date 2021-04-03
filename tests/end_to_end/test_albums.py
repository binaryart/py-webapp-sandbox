def test_index(client):
    rv = client.get("/albums")

    assert rv.status_code == 200

    json_data = rv.get_json()
    assert len(json_data["albums"]) == 2


def test_show(client):
    rv = client.get("/albums/1")

    assert rv.status_code == 200

    json_data = rv.get_json()
    assert json_data["album"]["id"] == 1
    assert json_data["album"]["artist"] == "John Mayer"
    assert json_data["album"]["name"] == "Room for Squares"


def test_create(client):
    rv = client.get("/albums")
    pre_albums_count = len(rv.get_json()["albums"])

    rv = client.post("/albums", json={"album": {"artist": "Noisettes", "name": "Wild Young Hearts"}})

    assert rv.status_code == 200

    json_data = rv.get_json()
    assert json_data["album"]["id"]
    assert json_data["album"]["artist"] == "Noisettes"
    assert json_data["album"]["name"] == "Wild Young Hearts"

    rv = client.get("/albums")
    assert len(rv.get_json()["albums"]) == pre_albums_count + 1


def test_update(client):
    rv = client.put("/albums/1", json={"album": {"artist": "Noisettes", "name": "What's the Time Mr Wolf?"}})

    assert rv.status_code == 200

    json_data = rv.get_json()
    assert json_data["album"]["id"] == 1
    assert json_data["album"]["artist"] == "Noisettes"
    assert json_data["album"]["name"] == "What's the Time Mr Wolf?"


def test_delete(client):
    rv = client.delete("/albums/1")

    assert rv.status_code == 204
    assert client.get("/albums/1").status_code == 404
