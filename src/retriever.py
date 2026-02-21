import faiss
from sklearn.preprocessing import normalize
from .embedder import Embedder

class NeuralRetriever:
    def __init__(self, dataframe):
        self.data = dataframe.reset_index(drop=True)
        self.embedder = Embedder()
        self._build_index()

    def _build_index(self):
        corpus = self.data["description"].tolist()
        embeddings = self.embedder.encode(corpus)
        embeddings = normalize(embeddings)

        self.index = faiss.IndexFlatIP(embeddings.shape[1])
        self.index.add(embeddings)

    def search(self, query: str, top_k: int = 5):
        q_emb = self.embedder.encode([query])
        q_emb = normalize(q_emb)

        scores, indices = self.index.search(q_emb, top_k)
        results = self.data.iloc[indices[0]].copy()
        results["score"] = scores[0]
        return results