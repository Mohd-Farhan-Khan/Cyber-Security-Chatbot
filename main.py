from src.config import *
from src.pdf_loader import load_documents
from src.text_splitter import split_documents
from src.embeddings import create_faiss_vectorstore
from src.rag_pipeline import setup_rag_pipeline
from src.interfaces.streamlit_app import run_streamlit_app

if __name__ == "__main__":
    run_streamlit_app()
