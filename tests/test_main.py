from fastapi.testclient import TestClient
from app import create_app

app = create_app()

client = TestClient(app)


def test_get_categories():
    response = client.get("/v1/categories")
    print(response.json())

    assert response.status_code == 200
