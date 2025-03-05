from fastapi import FastAPI
from app.routes import router
import uvicorn

# Initialize FastAPI
app = FastAPI(title="RAG-Based Q&A System", description="A FastAPI-based RAG System using CHROMA and LangChain")

# Include API routes
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to the RAG-Based Q&A System!"}


