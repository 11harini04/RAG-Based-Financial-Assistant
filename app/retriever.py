import faiss
import numpy as np

class FinancialVectorStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.docs = []

    def add_docs(self, embeddings, docs):
        self.index.add(np.array(embeddings))
        self.docs.extend(docs)

    def retrieve(self, query_embedding, k=3):
        if not self.docs:
            return []
        
        # Don't ask for more docs than we have
        k = min(k, len(self.docs))
        
        D, I = self.index.search(np.array(query_embedding), k)
        return [self.docs[i] for i in I[0]]