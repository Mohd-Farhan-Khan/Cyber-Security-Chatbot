#!/usr/bin/env python3
"""
Setup script to regenerate the FAISS vector database with your API key
"""

import os
import sys
import shutil

# Add the parent directory to the path to import from src
from pathlib import Path

# Get the project root directory
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.config import get_api_key, validate_api_key
from src.pdf_loader import load_documents
from src.text_splitter import split_documents
from src.embeddings import create_faiss_vectorstore

def setup_vector_database():
    """Setup the vector database from scratch"""
    
    print("🚀 Setting up Cyber Threat Chatbot Database...")
    print("=" * 50)
    
    # Check if API key is set
    if not validate_api_key():
        print("❌ Error: Please set your GOOGLE_API_KEY in the .env file first!")
        print("1. Get your API key from: https://makersuite.google.com/app/apikey")
        print("2. Replace 'YOUR_NEW_API_KEY_HERE' in .env file with your actual key")
        return False
    
    api_key = get_api_key()
    print(f"✅ API Key configured (ending with: ...{api_key[-10:]})")
    
    # Remove existing FAISS index if it exists
    index_path = "faiss_index_cyber"
    if os.path.exists(index_path):
        print(f"🗑️  Removing existing index: {index_path}")
        shutil.rmtree(index_path)
    
    try:
        # Load documents
        print("📄 Loading PDF documents...")
        file_paths = [
            "data/financial_services_cyber_threats_dataset.pdf",
            "data/Cyber Threat Sample.pdf",
            "data/Cyber Threat Sample1.pdf"
        ]
        
        all_docs = []
        for file_path in file_paths:
            if os.path.exists(file_path):
                print(f"   📖 Loading: {file_path}")
                docs = load_documents(file_path)
                all_docs.extend(docs)
            else:
                print(f"   ⚠️  File not found: {file_path}")
        
        if not all_docs:
            print("❌ No documents found to process!")
            return False
        
        print(f"✅ Loaded {len(all_docs)} document(s)")
        
        # Split documents
        print("✂️  Splitting documents into chunks...")
        chunks = split_documents(all_docs)
        print(f"✅ Created {len(chunks)} text chunks")
        
        # Create vector store
        print("🧠 Creating vector embeddings (this may take a few minutes)...")
        vectorstore = create_faiss_vectorstore(chunks, index_path)
        print(f"✅ Vector database created at: {index_path}")
        
        print("\n🎉 Setup completed successfully!")
        print("You can now run the chatbot with:")
        print("   streamlit run main.py")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during setup: {e}")
        return False

if __name__ == "__main__":
    success = setup_vector_database()
    if not success:
        exit(1)
