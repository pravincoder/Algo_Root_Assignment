# rag_system.py
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class RAGSystem:
    def __init__(self, functions):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.functions = functions
        docstrings = [func.__doc__ for func in functions]
        embeddings = self.model.encode(docstrings)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(np.array(embeddings))

    def retrieve_function(self, prompt):
        prompt_embedding = self.model.encode([prompt])
        D, I = self.index.search(np.array(prompt_embedding), k=1)
        return self.functions[I[0][0]].__name__