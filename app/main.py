from fastapi import FastAPI, File, UploadFile, Form
from rag import RAGPipeline
from utils import extract_text, query_llm
import uvicorn

app = FastAPI()
rag = RAGPipeline()

@app.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text(content)
    rag.add_documents([text])
    return {"message": "Document uploaded and processed."}

@app.post("/ask/")
async def ask_question(question: str = Form(...)):
    context = rag.retrieve(question)
    answer = query_llm(context, question)
    return {"answer": answer}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)

