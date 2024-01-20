from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_categories():
    response = client.get("/api/v1/categories")
    print(response.json())

    assert response.status_code == 200
