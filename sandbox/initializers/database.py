from sandbox.database import db_session


def init(flask_app):
    @flask_app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()
