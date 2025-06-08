from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class RAGPipeline:
    def __init__(self):
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(384)
        self.documents = []

    def add_documents(self, texts):
        embeddings = self.embedder.encode(texts)
        self.index.add(np.array(embeddings).astype('float32'))
        self.documents.extend(texts)

    def retrieve(self, query, k=3):
        query_vec = self.embedder.encode([query])
        D, I = self.index.search(np.array(query_vec).astype('float32'), k)
        return [self.documents[i] for i in I[0]]