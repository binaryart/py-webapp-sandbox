from flask import Flask

from sandbox.lib.flask_ext import errors
from sandbox.lib.flask_ext import resources
from sandbox.resources import health

from sandbox.resources import albums, album_songs


app = Flask(__name__)

# Register application middleware(s)
errors.register_error_handler(app)

# Diagnostic endpoint(s)
resources.register(app, "health", health)

# Domain Resource endpoints(s)
resources.register(app, "albums", albums)
resources.register(app, "albums/<int:album_id>/songs", album_songs)
