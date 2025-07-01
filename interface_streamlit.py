import streamlit as st
from pdf_loader import load_documents
from text_splitter import split_documents, print_token_stats
from embeddings import create_faiss_vectorstore
from rag_pipeline import setup_rag_pipeline

def run_streamlit_app():
    st.set_page_config(page_title="Cyber Threat Chatbot")
    st.title("🛡️ Cyber Threat Chatbot")

    file_path = "Cyber Threat Sample1.pdf" 

    with st.spinner("Processing PDF..."):
        try:
            documents = load_documents(file_path)
            chunks = split_documents(documents)
            print_token_stats(chunks)
            vectorstore = create_faiss_vectorstore(chunks)
            qa_chain = setup_rag_pipeline(vectorstore)
        except Exception as e:
            st.error(f"Failed to load PDF: {e}")
            return

    query = st.text_input("Ask a question about cyber threats:")
    if query:
        with st.spinner("Thinking..."):
            try:
                result = qa_chain({"query": query})
                st.success(result["result"])
                with st.expander("Sources"):
                    for doc in result["source_documents"]:
                        st.markdown(f"- {doc.page_content[:200]}...")
            except Exception as e:
                st.error(f"Error: {e}")
