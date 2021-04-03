import pytest

from sandbox.app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_root(client):
    rv = client.get("/?name=Jill")

    assert rv.status_code == 200
    assert b'Hello, Jill!' in rv.data

