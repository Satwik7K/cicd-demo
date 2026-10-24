from app import app

client = app.test_client()


def test_home_page():
    response = client.get("/")
    assert response.status_code == 200
    assert b"CI/CD pipeline" in response.data


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_add_endpoint():
    response = client.get("/add/2/3")
    assert response.status_code == 200
    assert response.get_json()["result"] == 5