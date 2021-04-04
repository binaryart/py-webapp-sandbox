import os
import shutil
import tempfile

import pytest
from dotenv import load_dotenv

# Load test specific environment variables
load_dotenv("../.env.test")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


@pytest.fixture
def client():
    db_fd, db_path = __new_test_database()
    os.environ["DATABASE_URL"] = f"sqlite:///{db_path}"

    from sandbox.app import create_app

    app = create_app()
    with app.test_client() as client:
        yield client

    try:
        os.unlink(db_path)
    finally:
        os.close(db_fd)


def __new_test_database():
    db_fd, db_path = tempfile.mkstemp()

    template_db = os.path.join(PROJECT_ROOT, os.getenv("DATABASE_FILE"))
    shutil.copyfile(template_db, db_path)

    return db_fd, db_path
