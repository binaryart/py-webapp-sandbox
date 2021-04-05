from flask import Flask

from sandbox.protocol.web.flask_hooks import errors, orm, resources
from sandbox.protocol.web.resources import albums, album_songs, health


def create_app():
    app = Flask(__name__)

    # Register application middleware(s)
    errors.register_error_handler(app)

    # Initialize application
    orm.init(app)

    # Diagnostic endpoint(s)
    resources.register(app, "health", health)

    # Domain Resource endpoints(s)
    resources.register(app, "albums", albums)
    resources.register(app, "albums/<int:album_id>/songs", album_songs)

    return app
