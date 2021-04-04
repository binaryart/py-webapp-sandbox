import pytest
from dotenv import load_dotenv

from sandbox.app import create_app


# Load test specific environment variables
load_dotenv("../.env.test")


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client
