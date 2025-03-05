from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.auth_service import AuthService
from app.rag import RAG
from app.database import SessionLocal, Document
from app.models import DocumentIngestRequest, QuestionRequest, AnswerResponse
from app.embeddings import generate_embedding
from app.services.retrieval_service import RetrievalService

router = APIRouter()
auth_service = AuthService()
rag_service = RAG()
retrieval_service = RetrievalService()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/ingest-document/")
async def ingest_document(doc: DocumentIngestRequest, db: Session = Depends(get_db)):
    """Stores document in PostgreSQL and indexes embeddings in ChromaDB."""
    
    # Generate embedding
    embedding = generate_embedding(doc.content)

    # Store in PostgreSQL
    new_doc = Document(name=doc.name, content=doc.content, embedding=embedding)
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)  # Get the generated `id`

    # Generate unique ID for ChromaDB
    doc_id = str(new_doc.id) if new_doc.id else str(uuid.uuid4())  # Use DB id or a new UUID

    # Index in ChromaDB
    retrieval_service.collection.add(
        ids=[doc_id],  # Unique document ID
        documents=[doc.content],  # Store document text
        embeddings=[embedding],   # Store vector embeddings
        metadatas=[{"name": doc.name}]  # Add metadata
    )

    return {"message": "Document ingested successfully", "document_id": new_doc.id}


### **RAG-Based Question Answering Endpoint**
@router.post("/ask-question/", response_model=AnswerResponse)
async def ask_question(question: QuestionRequest, user: dict = Depends(auth_service.verify_token)):
    """Handles user questions using RAG."""
    return rag_service.generate_answer(question.question)


## **Authentication Endpoint**
@router.post("/token")
async def login():
    """Simulates login and generates an access token."""
    return {"access_token": auth_service.create_access_token({"sub": "test_user"}), "token_type": "bearer"}
