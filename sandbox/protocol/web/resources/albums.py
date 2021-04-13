from flask import current_app, jsonify, make_response, request
from werkzeug.exceptions import NotFound

from sandbox.domain.models import generate_guid
from sandbox.domain.models.album import Album
from sandbox.persistence.orm.repositories.albums import SqlAlchemyAlbumRepository
from sandbox.protocol.web.serializers import serialize


def index():
    repository = SqlAlchemyAlbumRepository()

    albums = repository.find()
    return jsonify(albums=serialize(albums, as_list=True))


def show(guid):
    repository = SqlAlchemyAlbumRepository()

    album = repository.get(guid)
    if album:
        return jsonify(album=serialize(album))

    raise NotFound(description=f"Could not find album with guid {guid}.")


def create():
    repository = SqlAlchemyAlbumRepository()

    album_params = request.get_json()["album"]
    album_params["guid"] = generate_guid()

    album = Album(**album_params)
    repository.add(album)

    return jsonify(album=serialize(album))


def update(guid):
    repository = SqlAlchemyAlbumRepository()

    album = repository.get(guid)
    if album:
        album_params = request.get_json()["album"]
        for field, value in album_params.items():
            if hasattr(album, field):
                setattr(album, field, value)

        return jsonify(album=serialize(album))

    raise NotFound(description=f"Could not find album with guid {guid}.")


def delete(guid):
    repository = SqlAlchemyAlbumRepository()

    repository.remove(guid)

    response = make_response('', 204)
    response.mimetype = current_app.config['JSONIFY_MIMETYPE']
    return response
