import os
import shutil

import pytest
from dotenv import load_dotenv
from tests import PROJECT_ROOT

# Load test specific environment variables
load_dotenv(os.path.join(PROJECT_ROOT, ".env.test"))


@pytest.fixture
def client():
    db_path = __create_test_database()
    os.environ["DATABASE_URL"] = f"sqlite:///{db_path}"

    from sandbox.protocol.web.app import create_app

    app = create_app()
    with app.test_client() as client:
        yield client

    os.unlink(db_path)


def __create_test_database():
    template_db = os.path.join(PROJECT_ROOT, os.getenv("DATABASE_TEMPLATE_FILE"))
    db_path = os.path.join(PROJECT_ROOT, os.getenv("DATABASE_FILE"))
    shutil.copyfile(template_db, db_path)

    return db_path
