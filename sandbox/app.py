from flask import Flask

from sandbox.lib import resources
from sandbox.resources import health


app = Flask(__name__)

resources.register(app, "health", health)
