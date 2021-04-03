from dataclasses import dataclass
from flask import current_app, jsonify, make_response, request
from werkzeug.exceptions import NotFound


@dataclass
class Album:
    id: int
    name: str
    artist: str


in_memory_albums = [
    Album(id=1, name="Room for Squares", artist="John Mayer"),
    Album(id=2, name="St. Elsewhere", artist="Gnarls Barkley"),
]


def index():
    return jsonify(albums=in_memory_albums)


def show(id):
    for album in in_memory_albums:
        if album.id == id:
            return jsonify(album=album)

    raise NotFound(description=f"Could not find album with id {id}")


def create():
    global in_memory_albums

    album_params = request.get_json()["album"]
    album = Album(
        id=len(in_memory_albums) + 1,
        name=album_params["name"],
        artist=album_params["artist"],
    )
    in_memory_albums.append(album)

    return jsonify(album=album)


def update(id):
    album_params = request.get_json()["album"]

    for album in in_memory_albums:
        if album.id == id:
            album.name = album_params["name"]
            album.artist = album_params["artist"]

            return jsonify(album=album)

    raise NotFound(description=f"Could not find album with id {id}")


def delete(id):
    global in_memory_albums
    new_in_memory_albums = [
        album
        for album in in_memory_albums
        if album.id != id
    ]

    if len(new_in_memory_albums) != in_memory_albums:
        in_memory_albums = new_in_memory_albums

        response = make_response('', 204)
        response.mimetype = current_app.config['JSONIFY_MIMETYPE']
        return response
    else:
        raise NotFound(description=f"Could not find album with id {id}")

