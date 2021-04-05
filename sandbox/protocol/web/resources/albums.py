from flask import current_app, jsonify, make_response, request
from werkzeug.exceptions import NotFound

from sandbox.domain.repositories.errors import RecordNotFoundException

from sandbox.persistence.orm.models import Album
from sandbox.persistence.orm.repositories.albums import SqlAlchemyAlbumRepository
from sandbox.protocol.web.serializers import serialize


def index():
    repository = SqlAlchemyAlbumRepository()

    albums = repository.find()
    return jsonify(albums=serialize(albums, as_list=True))


def show(id):
    repository = SqlAlchemyAlbumRepository()

    album = repository.get(id)
    if album:
        return jsonify(album=serialize(album))

    raise NotFound(description=f"Could not find album with id {id}.")


def create():
    repository = SqlAlchemyAlbumRepository()

    album_params = request.get_json()["album"]

    album = Album(**album_params)
    repository.add(album)

    return jsonify(album=serialize(album))


def update(id):
    repository = SqlAlchemyAlbumRepository()

    album = repository.get(id)
    if album:
        album_params = request.get_json()["album"]
        for field, value in album_params.items():
            if hasattr(album, field):
                setattr(album, field, value)

        return jsonify(album=serialize(album))

    raise NotFound(description=f"Could not find album with id {id}.")


def delete(id):
    repository = SqlAlchemyAlbumRepository()

    try:
        repository.remove(id)

        response = make_response('', 204)
        response.mimetype = current_app.config['JSONIFY_MIMETYPE']
        return response
    except RecordNotFoundException:
        raise NotFound(description=f"Could not find album with id {id}.")
