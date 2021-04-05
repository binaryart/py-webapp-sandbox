from dataclasses import dataclass
from flask import jsonify
from werkzeug.exceptions import NotFound


@dataclass
class Song:
    id: int
    album_id: int
    name: str


in_memory_songs = [
    Song(id=1, album_id=1, name="No Such Thing"),
    Song(id=2, album_id=1, name="Why Georgia"),
    Song(id=3, album_id=1, name="My Stupid Mouth"),
    Song(id=4, album_id=1, name="Your Body Is a Wonderland"),
    Song(id=5, album_id=1, name="Neon"),
    Song(id=6, album_id=1, name="City Love"),
    Song(id=7, album_id=1, name="83"),
    Song(id=8, album_id=1, name="3x5"),
    Song(id=9, album_id=1, name="Love Song for No One"),
    Song(id=10, album_id=1, name="Back to You"),
    Song(id=11, album_id=1, name="Great Indoors"),
    Song(id=12, album_id=1, name="Not Myself"),
    Song(id=13, album_id=1, name="St. Patrick's Day"),
]


def index(album_id):
    songs = [
        s
        for s in in_memory_songs
        if s.album_id == album_id
    ]

    if songs:
        return jsonify(songs=songs)
    else:
        raise NotFound(description=f"Could not find songs for album id {album_id}.")


def show(album_id, id):
    for song in in_memory_songs:
        if song.id == id and song.album_id == album_id:
            return jsonify(song=song)

    raise NotFound(description=f"Could not find song with id {id} for album id {album_id}.")

