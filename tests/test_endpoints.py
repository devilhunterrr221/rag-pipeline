from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload():
    with open("tests/sample.pdf", "rb") as f:
        response = client.post("/upload/", files={"file": ("sample.pdf", f, "application/pdf")})
    assert response.status_code == 200
    assert "Document uploaded" in response.json()["message"]

def test_ask():
    response = client.post("/ask/", data={"question": "What is this about?"})
    assert response.status_code == 200
    assert "answer" in response.json()