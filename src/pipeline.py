from .data_loader import load_orphadata
from .ontology_parser import OntologyParser
from .retriever import NeuralRetriever

class RareDiseasePipeline:
    def __init__(self, ontology_path: str, dataset_path: str):
        self.ontology = OntologyParser(ontology_path)
        df = load_orphadata(dataset_path)
        self.retriever = NeuralRetriever(df)

    def predict(self, query: str):
        expanded_terms = self.ontology.expand_terms(query)
        enriched_query = query + " " + " ".join(expanded_terms)
        return self.retriever.search(enriched_query)