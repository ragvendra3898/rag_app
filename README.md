# RAG-Based Q&A System

This project implements a **Retrieval-Augmented Generation (RAG) Q&A system** using **FastAPI, PostgreSQL, FAISS, and LangChain**. 

## Features
**FastAPI-based backend**  
**Document Ingestion, Retrieval, and RAG-based Q&A**  
**JWT Authentication for Security**  
**CHROMA for Fast Similarity Search**  
**PostgreSQL for Metadata Storage**  
**Automated Testing & CI/CD Integration**  
**Dockerized for Easy Deployment**  

---

## 1. Installation

### Prerequisites
- **Python 3.11+**
- **PostgreSQL**
- **Docker** (optional for containerized deployment)

### Clone the Repository
```bash
git clone https://github.com/your-username/rag-app.git
cd rag-app
```

### 🔹 Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 🔹 Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 2. Database Setup

### Configure PostgreSQL
```sql
CREATE DATABASE rag_db;
CREATE USER rag_user WITH ENCRYPTED PASSWORD 'securepassword';
GRANT ALL PRIVILEGES ON DATABASE rag_db TO rag_user;
```

### Initialize Database
```bash
python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"
```

---

## 3. Running the API

### Start FastAPI Server
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
✅ FastAPI runs at: [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs)

---

## 4. Testing API Endpoints

### Ingest a Document
```bash
curl -X POST "http://127.0.0.1:8000/ingest-document/" -H "Content-Type: application/json" -d '{"name": "Test Doc", "content": "This is a test"}'
```

### Ask a Question
```bash
curl -X POST "http://127.0.0.1:8000/ask-question/" -H "Content-Type: application/json" -d '{"question": "What is RAG?"}'
```

---

## 5. Running with Docker

### Build and Start Containers
```bash
docker-compose up --build
```

### Check Running Containers
```bash
docker ps
```

---

## 📌 6. Running Tests

### Execute Unit Tests
```bash
pytest --cov=app tests/
```
✅ Ensure **75%+ test coverage**.

---

## 7. GitHub CI/CD Pipeline

This project includes a **GitHub Actions CI/CD pipeline** that:
- Runs **automated tests** on each push to `main` or `dev`.
- Ensures **code quality** before merging.

### GitHub Actions Workflow
`.github/workflows/ci.yml`
```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ "main", "dev" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout Code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: '3.11'

    - name: Install Dependencies
      run: pip install -r requirements.txt

    - name: Run Tests
      run: pytest tests/
```

✅ **Each push triggers CI/CD tests automatically.**

---

## 8. Deployment

### Deploy to Azure (Example)
```bash
az webapp up --name my-rag-app --resource-group my-group
```
✅ **Your API is now live!**

---

## 9. Contributing

1. **Fork the repository**
2. **Create a feature branch** (`feature/your-feature`)
3. **Commit changes** (`git commit -m "Added feature X"`)
4. **Push to GitHub** (`git push origin feature/your-feature`)
5. **Open a Pull Request**

---

## 10. License

This project is licensed under the **MIT License**.

---

## 11. Contact

📧 **Email:** your-email@example.com  
🔗 **GitHub:** [your-github-profile](https://github.com/your-username)  

---

✅ **Your project is now fully documented!** 🚀  
