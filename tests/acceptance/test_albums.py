def test_albums(client):
    # fresh database
    rv = client.get("/albums")

    assert rv.status_code == 200
    assert len(rv.get_json()["albums"]) == 0

    # create albums
    rv = client.post("/albums", json={"album": {"artist": "John Mayer", "name": "Room for Squares"}})

    assert rv.status_code == 200
    room_for_squares = rv.get_json()
    assert room_for_squares["album"]["id"] == 1
    assert room_for_squares["album"]["artist"] == "John Mayer"
    assert room_for_squares["album"]["name"] == "Room for Squares"

    rv = client.post("/albums", json={"album": {"artist": "Gnarls Barkley", "name": "St. Elsewhere"}})

    assert rv.status_code == 200
    st_elsewhere = rv.get_json()
    assert st_elsewhere["album"]["id"] == 2
    assert st_elsewhere["album"]["artist"] == "Gnarls Barkley"
    assert st_elsewhere["album"]["name"] == "St. Elsewhere"

    rv = client.post("/albums", json={"album": {"artist": "Noisettes", "name": "Wild Young Hearts"}})
    assert rv.status_code == 200
    wild_young_heart = rv.get_json()
    assert wild_young_heart["album"]["id"] == 3
    assert wild_young_heart["album"]["artist"] == "Noisettes"
    assert wild_young_heart["album"]["name"] == "Wild Young Hearts"

    # after creating entries
    rv = client.get("/albums")

    assert rv.status_code == 200
    assert len(rv.get_json()["albums"]) == 3

    # can read details of an album
    rv = client.get("/albums/1")

    assert rv.status_code == 200
    assert rv.get_json() == room_for_squares

    # update an album
    rv = client.put("/albums/3", json={"album": {"artist": "Noisettes", "name": "What's the Time Mr Wolf?"}})

    assert rv.status_code == 200
    whats_the_time_mr_wolf = rv.get_json()
    assert whats_the_time_mr_wolf["album"]["id"] == 3
    assert whats_the_time_mr_wolf["album"]["artist"] == "Noisettes"
    assert whats_the_time_mr_wolf["album"]["name"] == "What's the Time Mr Wolf?"

    # delete an album
    rv = client.delete("/albums/1")

    assert rv.status_code == 204
    assert client.get("/albums/1").status_code == 404
    assert len(client.get("/albums").get_json()["albums"]) == 2

    # cannot delete deleted album
    rv = client.put("/albums/1", json={"album": {"artist": "John Mayer", "name": "Room for Squares"}})

    assert rv.status_code == 404


#
#
# def test_show(client):
#     rv = client.get("/albums/1")
#
#     assert rv.status_code == 200
#
#     json_data = rv.get_json()
#     assert json_data["album"]["id"] == 1
#     assert json_data["album"]["artist"] == "John Mayer"
#     assert json_data["album"]["name"] == "Room for Squares"


# def test_create(client):
#     rv = client.get("/albums")
#     pre_albums_count = len(rv.get_json()["albums"])
#
#     rv = client.post("/albums", json={"album": {"artist": "Noisettes", "name": "Wild Young Hearts"}})
#
#     assert rv.status_code == 200
#
#     json_data = rv.get_json()
#     assert json_data["album"]["id"]
#     assert json_data["album"]["artist"] == "Noisettes"
#     assert json_data["album"]["name"] == "Wild Young Hearts"
#
#     rv = client.get("/albums")
#     assert len(rv.get_json()["albums"]) == pre_albums_count + 1
#
#
# def test_update(client):
#     rv = client.put("/albums/1", json={"album": {"artist": "Noisettes", "name": "What's the Time Mr Wolf?"}})
#
#     assert rv.status_code == 200
#
#     json_data = rv.get_json()
#     assert json_data["album"]["id"] == 1
#     assert json_data["album"]["artist"] == "Noisettes"
#     assert json_data["album"]["name"] == "What's the Time Mr Wolf?"
#
#
# def test_delete(client):
#     rv = client.delete("/albums/1")
#
#     assert rv.status_code == 204
#     assert client.get("/albums/1").status_code == 404
