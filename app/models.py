from pydantic import BaseModel
from typing import List

# Model for document ingestion API request
class DocumentIngestRequest(BaseModel):
    name: str
    content: str

# Model for question API request
class QuestionRequest(BaseModel):
    question: str

# Model for response containing answer and source documents
class AnswerResponse(BaseModel):
    answer: str
    source_documents: List[str]
