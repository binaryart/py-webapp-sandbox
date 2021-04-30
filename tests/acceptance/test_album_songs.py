def test_should_get_song(client):
    # when: we ask for specific song for an album
    album_guid = "1"
    song_guid = "13"
    rv = client.get(f"/albums/{album_guid}/songs/{song_guid}")

    # then: system returns the song
    song = rv.get_json()["song"]
    assert song["guid"] == song_guid
    assert song["album_guid"] == album_guid
    assert song["name"] == "St. Patrick's Day"


def test_should_list_songs(client):
    # when: we ask for all songs for an album
    album_guid = "1"
    rv = client.get(f"/albums/{album_guid}/songs")

    # then: system returns the songs for the album
    songs = rv.get_json()["songs"]
    assert len(songs) == 13
