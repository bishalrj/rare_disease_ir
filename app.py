import streamlit as st
from src.pipeline import RareDiseasePipeline

pipeline = RareDiseasePipeline(
    ontology_path="data/doid.owl",
    dataset_path="data/orphadata_2026.csv"
)

st.title("Ontology-Driven Neural IR for Rare Disease Detection")

query = st.text_input("Enter patient symptoms")

if query:
    results = pipeline.predict(query)
    st.subheader("By Prediction, We can say that")
    st.dataframe(results)