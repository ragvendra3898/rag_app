import openai
from app.services.retrieval_service import RetrievalService

class RAG:
    def __init__(self):
        self.retriever = RetrievalService()

    def generate_answer(self, query: str):
        """Fetch relevant documents and generate an answer."""
        source_documents = self.retriever.retrieve(query)

        if not source_documents:
            return {"answer": "No relevant documents found.", "source_documents": []}
        
        source_documents = [str(doc) for doc in source_documents]

        # Format retrieved documents for the LLM
        context = "\n\n".join(source_documents)

        

        response = openai.Client().chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an AI assistant answering questions based on retrieved documents."},
                {"role": "user", "content": f"Based on the following documents, answer this question:\n\n{context}\n\n{query}"}
            ]
        )

        answer = response.choices[0].message.content
        return {"answer": answer, "source_documents": source_documents}
