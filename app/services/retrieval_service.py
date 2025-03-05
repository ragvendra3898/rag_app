from chromadb import PersistentClient
from app.embeddings import generate_embedding 

class RetrievalService:
    def __init__(self):
        self.client = PersistentClient(path="/chroma")  # Ensure this path is correct
        self.collection = self.client.get_or_create_collection("documents")

    def retrieve(self, query: str, top_k: int = 5):
        """Fetches the most relevant documents based on the query."""
        query_embedding = generate_embedding(query)  # Generate query embedding

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        # Extract relevant documents
        source_docs = results.get("documents", [])
        return source_docs
