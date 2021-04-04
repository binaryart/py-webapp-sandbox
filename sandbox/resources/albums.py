from flask import current_app, jsonify, make_response, request
from werkzeug.exceptions import NotFound

from sandbox.database import db_session
from sandbox.models import Album
from sandbox.serializers import serialize


def index():
    albums = db_session.query(Album).all()
    return jsonify(albums=serialize(albums, as_list=True))


def show(id):
    album = db_session.query(Album).filter_by(id=id).first()
    if album:
        return jsonify(album=serialize(album))

    raise NotFound(description=f"Could not find album with id {id}.")


def create():
    album_params = request.get_json()["album"]

    album = Album(**album_params)
    db_session.add(album)
    db_session.commit()

    return jsonify(album=serialize(album))


def update(id):
    album = db_session.query(Album).filter_by(id=id).first()
    if album:
        album_params = request.get_json()["album"]
        for field, value in album_params.items():
            if hasattr(album, field):
                setattr(album, field, value)

        return jsonify(album=serialize(album))

    raise NotFound(description=f"Could not find album with id {id}.")


def delete(id):
    album = db_session.query(Album).filter_by(id=id).first()
    if album:
        db_session.delete(album)

        response = make_response('', 204)
        response.mimetype = current_app.config['JSONIFY_MIMETYPE']
        return response

    raise NotFound(description=f"Could not find album with id {id}.")
