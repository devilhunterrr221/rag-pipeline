# Retrieval-Augmented Generation (RAG) Pipeline

This project is a RAG-based QA system allowing users to upload documents and ask questions over their content using OpenAI's GPT-4.

## Features
- Upload PDF files
- Query documents with natural language
- Fast vector retrieval using FAISS
- LLM response generation
- Containerized with Docker

## Setup Instructions
```bash
git clone https://github.com/yourusername/rag-pipeline.git
cd rag-pipeline
```

### Run Locally
```bash
pip install -r requirements.txt
export OPENAI_API_KEY=your_key
uvicorn app.main:app --reload
```

### Run with Docker
```bash
docker build -t rag-pipeline .
docker run -p 8000:8000 -e OPENAI_API_KEY=your_key rag-pipeline
```

### API Endpoints
- `POST /upload/` - Upload a PDF document
- `POST /ask/` - Ask a question related to uploaded documents

### Postman
Import `postman_collection.json` to test endpoints.

### Testing
```bash
pytest tests/
```