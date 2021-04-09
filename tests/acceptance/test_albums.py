def test_should_get_created_album(client):
    album_params = {"album": {"artist": "Noisettes", "name": "Wild Young Hearts"}}

    # when: we create an album
    rv = client.post("/albums", json=album_params)
    album_guid = rv.get_json()["album"]["guid"]

    # then: we should be able to read it back
    rv = client.get(f"/albums/{album_guid}")
    album = rv.get_json()["album"]
    assert album["artist"] == "Noisettes"
    assert album["name"] == "Wild Young Hearts"


def test_should_list_albums(client):
    # given: we have two albums in system
    client.post("/albums", json={"album": {"artist": "John Mayer", "name": "Room for Squares"}})
    client.post("/albums", json={"album": {"artist": "Gnarls Barkley", "name": "St. Elsewhere"}})

    # when: we ask for all albums
    rv = client.get("/albums")

    # then: system returns the albums we have added
    albums = rv.get_json()["albums"]
    assert len(albums) == 2
    assert albums[0]["guid"]
    assert albums[0]["artist"] == "John Mayer"
    assert albums[0]["name"] == "Room for Squares"
    assert albums[1]["guid"]
    assert albums[1]["artist"] == "Gnarls Barkley"
    assert albums[1]["name"] == "St. Elsewhere"


def test_should_get_updated_album(client):
    # given: we created an album
    rv = client.post("/albums", json={"album": {"artist": "Noisettes", "name": "Wild Young Hearts"}})
    album_guid = rv.get_json()["album"]["guid"]

    # when: we update the album
    client.put(f"/albums/{album_guid}", json={"album": {"artist": "Noisettes", "name": "What's the Time Mr Wolf?"}})

    # then: we should see updated album
    rv = client.get(f"/albums/{album_guid}")
    album = rv.get_json()["album"]
    assert rv.status_code == 200
    assert album["artist"] == "Noisettes"
    assert album["name"] == "What's the Time Mr Wolf?"


def test_should_delete_album(client):
    # given: we have an album
    rv = client.post("/albums", json={"album": {"artist": "John Mayer", "name": "Room for Squares"}})
    album_guid = rv.get_json()["album"]["guid"]

    # when: we delete the album
    client.delete(f"/albums/{album_guid}")

    # then: we should not be able to access the album
    assert client.get(f"/albums/{album_guid}").status_code == 404
