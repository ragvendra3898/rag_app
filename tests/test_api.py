from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_document_ingestion():
    response = client.post("/ingest-document/", json={"name": "Test Doc", "content": "Sample text"})
    assert response.status_code == 200

def test_ask_question():
    response = client.post("/ask-question/", json={"question": "What is RAG?"})
    assert response.status_code == 200
