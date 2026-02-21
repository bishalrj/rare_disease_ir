# src/ontology_parser.py

class OntologyParser:
    def __init__(self, ontology_path: str):
        # Disabled ontology loading due to Python 3.14 compatibility issues
        self.onto = None

    def expand_terms(self, query: str):
        # No ontology expansion for now
        return []