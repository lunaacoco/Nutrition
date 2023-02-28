import pytest
from app.app import create_app


#This gets executed everytime we run a test because we need the Flask app to test anything in it
@pytest.fixture
def client():
    app = create_app()

    with app.app_context():
        yield app.test_client()
