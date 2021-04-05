from werkzeug.exceptions import InternalServerError
from sandbox.persistence.orm.database import db_session


def init(flask_app):
    from sandbox.persistence.orm import mappers
    _ = mappers  # suppress unused import warning and not let linters remove mappers invocation

    flask_app.after_request(__commit_request_transaction)
    flask_app.teardown_appcontext(__shutdown_session)


def __commit_request_transaction(response):
    if 200 <= response.status_code < 400:
        try:
            db_session.commit()
        except Exception:
            raise InternalServerError()
    else:
        db_session.rollback()
    return response


def __shutdown_session(exception=None):
    db_session.remove()
