import json
from sqlalchemy.orm import Session
from app.database import Document
from app.embeddings import generate_embedding 

class DocumentService:
    def __init__(self, db: Session):
        self.db = db

    def ingest_document(self, name: str, content: str):
        """Stores document data in the database with embeddings."""
        embedding = generate_embedding(content)  # Ensure embedding is generated

        if not isinstance(embedding, list):  # Ensure `embedding` is a list
            raise ValueError("Embedding must be a list")

        new_doc = Document(
            name=name,
            content=content,
            embedding=json.dumps(embedding)  
        )

        self.db.add(new_doc)
        self.db.commit()
        return {"message": "Document stored successfully", "document_id": new_doc.id}
