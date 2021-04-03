from flask import jsonify


def index():
    return jsonify(status="ok")
