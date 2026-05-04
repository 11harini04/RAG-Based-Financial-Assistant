import streamlit as st
import requests
from urllib.parse import quote

st.title("Financial RAG Assistant")

# Sidebar for document ingestion
with st.sidebar:
    st.header("Document Management")
    doc_text = st.text_area("Paste financial documents here:")
    if st.button("Ingest Documents"):
        if not doc_text.strip():
            st.warning("Please paste some documents first")
        else:
            try:
                res = requests.post(f"http://localhost:8000/ingest", json={"docs": [doc_text]})
                res.raise_for_status()
                st.success("Documents ingested successfully!")
            except Exception as e:
                st.error(f"Failed to ingest: {str(e)}")

st.info("💡 **Tip:** Ingest financial documents from the sidebar first, then ask questions about them!")

query = st.text_input("Ask financial question")

if st.button("Analyze"):
    if not query.strip():
        st.warning("Please enter a question")
    else:
        with st.spinner("Processing query... (first request may take 30s to load models)"):
            try:
                res = requests.get(f"http://localhost:8000/ask?q={quote(query)}", timeout=30)
                res.raise_for_status()
                data = res.json()
                st.success(data["response"])
            except requests.exceptions.ConnectionError:
                st.error("Cannot connect to backend. Make sure uvicorn is running on http://localhost:8000")
            except requests.exceptions.Timeout:
                st.error("Request timeout (30s). Backend is still loading. Try again in a moment.")
            except requests.exceptions.HTTPError as e:
                st.error(f"Backend error: {e.response.status_code} - {e.response.text}")
            except Exception as e:
                st.error(f"Error: {str(e)}")