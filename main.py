from config import *
from pdf_loader import load_documents
from text_splitter import split_documents
from embeddings import create_faiss_vectorstore
from rag_pipeline import setup_rag_pipeline
from interface_streamlit import run_streamlit_app
from interface_cli import run_chatbot_cli

MODE = "streamlit"  # Change to "cli" if needed

if MODE == "streamlit":
    run_streamlit_app()
else:
    file_path = "Cyber Threat Sample1.pdf"
    docs = load_documents(file_path)
    chunks = split_documents(docs)
    vectorstore = create_faiss_vectorstore(chunks)
    qa_chain = setup_rag_pipeline(vectorstore)
    run_chatbot_cli(qa_chain)
