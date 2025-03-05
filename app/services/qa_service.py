from app.embeddings import retrieve_similar_docs
from app.database import SessionLocal, Document

class QAService:
    def __init__(self, db: SessionLocal):
        self.db = db

    def ask_question(self, question: str):
        similar_docs = retrieve_similar_docs(question)
        docs = self.db.query(Document).filter(Document.id.in_(similar_docs)).all()
        return {"answer": f"Based on {len(docs)} relevant documents, the answer is generated.",
                "source_documents": [doc.name for doc in docs]}
