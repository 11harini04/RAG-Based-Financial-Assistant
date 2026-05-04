User Query
   ↓
Embedding Model
   ↓
FAISS Vector DB (Financial Docs)
   ↓
Retriever (Top-K chunks)
   ↓
LLM (Groq)
   ↓
Guardrails + Structured Output
   ↓
Final Answer

**********************************************************
financial-rag-assistant/
│── app/
│   ├── main.py
│   ├── rag_pipeline.py
│   ├── llm.py
│   ├── embeddings.py
│   ├── retriever.py
│   ├── guardrails.py
│
│── data/
│   ├── finance_docs.txt
│
│── ui/
│   ├── app.py
│
│── .env
│── requirements.txt
│── README.md