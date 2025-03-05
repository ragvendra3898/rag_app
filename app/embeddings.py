import chromadb
from langchain_openai import OpenAIEmbeddings

# Initialize ChromaDB client (persistent storage)
chroma_client = chromadb.PersistentClient(path="./chroma_db")

# Create a collection for document embeddings
collection = chroma_client.get_or_create_collection(name="documents")

# Initialize embedding model
embedding_model = OpenAIEmbeddings()

def generate_embedding(text: str):
    """Generates an embedding for the given text."""
    return embedding_model.embed_query(text)

def store_embedding(doc_id: str, text: str):
    """Stores document embedding in ChromaDB."""
    embedding = generate_embedding(text)
    collection.add(
        ids=[str(doc_id)], 
        embeddings=[embedding], 
        metadatas=[{"content": text}]
    )

def retrieve_similar_docs(query: str, top_k=3):
    """Retrieves top-K similar documents using ChromaDB."""
    query_embedding = generate_embedding(query)
    results = collection.query(
        query_embeddings=[query_embedding], 
        n_results=top_k
    )
    return results["ids"][0]  # Return list of matching document IDs
