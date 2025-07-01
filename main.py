from src.config import *
from src.pdf_loader import load_documents
from src.text_splitter import split_documents
from src.embeddings import create_faiss_vectorstore
from src.rag_pipeline import setup_rag_pipeline
from src.interfaces.streamlit_app import run_streamlit_app
from src.interfaces.cli_app import run_chatbot_cli

MODE = "streamlit"  # Change to "cli" if needed

if MODE == "streamlit":
    run_streamlit_app()
else:
    file_path = "data/financial_services_cyber_threats_dataset.pdf"
    docs = load_documents(file_path)
    chunks = split_documents(docs)
    vectorstore = create_faiss_vectorstore(chunks)
    qa_chain = setup_rag_pipeline(vectorstore)
    run_chatbot_cli(qa_chain)
