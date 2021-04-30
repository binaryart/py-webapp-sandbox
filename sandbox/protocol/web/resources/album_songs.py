from dataclasses import dataclass
from flask import jsonify
from werkzeug.exceptions import NotFound

from sandbox.protocol.web.serializers import serialize


@dataclass
class Song:
    guid: str
    album_guid: str
    name: str


in_memory_songs = [
    Song(guid="1", album_guid="1", name="No Such Thing"),
    Song(guid="2", album_guid="1", name="Why Georgia"),
    Song(guid="3", album_guid="1", name="My Stupid Mouth"),
    Song(guid="4", album_guid="1", name="Your Body Is a Wonderland"),
    Song(guid="5", album_guid="1", name="Neon"),
    Song(guid="6", album_guid="1", name="City Love"),
    Song(guid="7", album_guid="1", name="83"),
    Song(guid="8", album_guid="1", name="3x5"),
    Song(guid="9", album_guid="1", name="Love Song for No One"),
    Song(guid="10", album_guid="1", name="Back to You"),
    Song(guid="11", album_guid="1", name="Great Indoors"),
    Song(guid="12", album_guid="1", name="Not Myself"),
    Song(guid="13", album_guid="1", name="St. Patrick's Day"),
]


def index(album_guid):
    songs = [
        s
        for s in in_memory_songs
        if s.album_guid == album_guid
    ]

    if songs:
        return jsonify(songs=serialize(songs, as_list=True))
    else:
        raise NotFound(description=f"Could not find songs for album id {album_guid}.")


def show(album_guid, guid):
    for song in in_memory_songs:
        if song.guid == guid and song.album_guid == album_guid:
            return jsonify(song=serialize(song))

    raise NotFound(description=f"Could not find song with id {guid} for album id {album_guid}.")
