from fastapi import FastAPI
from .rag_pipeline import ingest_documents, process_query

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Financial RAG Assistant API", "docs": "/docs"}

@app.post("/ingest")
def ingest(docs: list[str]):
    ingest_documents(docs)
    return {"status": "Documents ingested"}

@app.get("/ask")
def ask(q: str):
    answer = process_query(q)
    return {"response": answer}