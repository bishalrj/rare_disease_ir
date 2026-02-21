import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from .embedder import Embedder

class NeuralRetriever:
    def __init__(self, dataframe):
        self.data = dataframe.reset_index(drop=True)
        self.embedder = Embedder()
        self._build_index()

    def _build_index(self):
        corpus = self.data["description"].tolist()
        self.embeddings = self.embedder.encode(corpus)

    def search(self, query: str, top_k: int = 5):
        q_emb = self.embedder.encode([query])
        scores = cosine_similarity(q_emb, self.embeddings)[0]

        top_idx = scores.argsort()[-top_k:][::-1]
        results = self.data.iloc[top_idx].copy()
        results["score"] = scores[top_idx]
        return results
