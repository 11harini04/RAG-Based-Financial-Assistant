from .embeddings import embed_text
from .retriever import FinancialVectorStore
from .llm import generate_financial_answer
from .guardrails import validate_response

vectorstore = FinancialVectorStore(dim=384)

def ingest_documents(docs):
    embeddings = embed_text(docs)
    vectorstore.add_docs(embeddings, docs)

def process_query(query):
    q_emb = embed_text([query])
    retrieved_docs = vectorstore.retrieve(q_emb)

    context = "\n".join(retrieved_docs)

    raw_answer = generate_financial_answer(context, query)
    final_answer = validate_response(raw_answer)

    return final_answer