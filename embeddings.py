from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

def create_faiss_vectorstore(chunks, index_name="faiss_index_cyber"):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(index_name)
    return vectorstore

def load_faiss_vectorstore(index_name="faiss_index_cyber"):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    return FAISS.load_local(index_name, embeddings)
