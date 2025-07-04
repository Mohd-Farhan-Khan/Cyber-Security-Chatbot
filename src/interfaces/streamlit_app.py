import streamlit as st
import time
from datetime import datetime
from src.pdf_loader import load_documents
from src.text_splitter import split_documents
from src.embeddings import create_faiss_vectorstore
from src.rag_pipeline import setup_rag_pipeline

def initialize_session_state():
    """Initialize session state variables for the chatbot"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "qa_chain" not in st.session_state:
        st.session_state.qa_chain = None
    if "documents_loaded" not in st.session_state:
        st.session_state.documents_loaded = False
    if "selected_question" not in st.session_state:
        st.session_state.selected_question = ""
    if "input_text" not in st.session_state:
        st.session_state.input_text = ""

def load_and_process_documents():
    """Load and process PDF documents with progress tracking"""
    file_path = "data/financial_services_cyber_threats_dataset.pdf"
    
    with st.status("🔄 Initializing Cyber Threat Intelligence System...", expanded=True) as status:
        try:
            # st.write("📄 Loading PDF document...")
            documents = load_documents(file_path)

            # st.write("✂️ Splitting document into chunks...")
            chunks = split_documents(documents)

            # st.write("🧠 Creating vector embeddings...")
            vectorstore = create_faiss_vectorstore(chunks)

            # st.write("⚡ Setting up RAG pipeline...")
            qa_chain = setup_rag_pipeline(vectorstore)
            
            st.session_state.qa_chain = qa_chain
            st.session_state.documents_loaded = True
            
            status.update(label="✅ System Ready!", state="complete", expanded=False)
            time.sleep(0.5)  # Brief pause for visual feedback
            
        except Exception as e:
            status.update(label="❌ System Error", state="error", expanded=True)
            st.error(f"Failed to initialize system: {e}")
            return False
    
    return True

def display_system_info():
    """Display system information and document status"""
    with st.sidebar:
        st.subheader("💡 Sample Questions")
        sample_questions = [
            "What are the main cybersecurity threats?",
            "How can organizations protect against ransomware?",
            "What are the best practices for incident response?",
            "Explain the current threat landscape.",
            "What security measures are recommended?"
        ]
        
        for question in sample_questions:
            if st.button(question, key=f"sample_{hash(question)}", use_container_width=True):
                st.session_state.input_text = question
                st.rerun()

def display_chat_message(role, content, sources=None):
    """Display a chat message with proper formatting"""
    with st.chat_message(role):
        if role == "assistant":
            st.write(content)
            if sources and len(sources) > 0:
                with st.expander(f"📚 Sources ({len(sources)} references)", expanded=False):
                    for i, doc in enumerate(sources, 1):
                        st.markdown(f"""
                        **Source {i}:**
                        ```
                        {doc.page_content[:300]}...
                        ```
                        """)
        else:
            st.write(content)

def run_streamlit_app():
    # Configure page
    st.set_page_config(
        page_title="Cyber Threat Intelligence Chatbot",
        page_icon="🛡️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .chat-container {
        max-height: 400px;
        overflow-y: auto;
        padding: 1rem;
        border: 1px solid #ddd;
        border-radius: 10px;
        background-color: #f8f9fa;
    }
    .stButton > button {
        width: 100%;
        margin: 0.25rem 0;
    }
    .stTextInput > div > div > input {
        border-radius: 20px;
        border: 2px solid #e0e0e0;
        padding: 10px 15px;
        font-size: 14px;
    }
    .stTextInput > div > div > input:focus {
        border-color: #1e3c72;
        box-shadow: 0 0 0 2px rgba(30, 60, 114, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🛡️ Cyber Threat Intelligence Chatbot</h1>
        <p>Your AI-powered cybersecurity analyst</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    initialize_session_state()
    
    # Display system information in sidebar
    display_system_info()
    
    # Main content area
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Load documents if not already loaded
        if not st.session_state.documents_loaded:
            if not load_and_process_documents():
                st.stop()
        
        # Welcome message
        if not st.session_state.messages:
            st.session_state.messages.append({
                "role": "assistant",
                "content": "👋 Hello! I'm your Cyber Threat Intelligence assistant. I've analyzed cybersecurity documents and I'm ready to answer your questions about threats, vulnerabilities, and security best practices. How can I help you today?",
                "sources": None
            })
        
        # Display chat history
        st.subheader("💬 Conversation")
        for message in st.session_state.messages:
            display_chat_message(message["role"], message["content"], message.get("sources"))
        
        # Chat input
        with st.form("chat_form", clear_on_submit=True):
            col_input, col_button = st.columns([4, 1])
            
            with col_input:
                user_input = st.text_input(
                    "Ask me about cybersecurity threats...",
                    value=st.session_state.input_text,
                    key="chat_input",
                    label_visibility="collapsed",
                    placeholder="Ask me about cybersecurity threats..."
                )
            
            with col_button:
                submit_clicked = st.form_submit_button("Send", type="primary", use_container_width=True)
        
        # Process input when Send button is clicked or Enter is pressed
        if submit_clicked and user_input.strip():
            prompt = user_input.strip()
            # Clear the input field after sending
            st.session_state.input_text = ""
            
            # Add user message
            st.session_state.messages.append({
                "role": "user", 
                "content": prompt,
                "sources": None
            })
            display_chat_message("user", prompt)
            
            # Get AI response
            with st.chat_message("assistant"):
                with st.spinner("🤔 Analyzing threat intelligence..."):
                    try:
                        result = st.session_state.qa_chain.invoke({"query": prompt})
                        response_content = result["result"]
                        sources = result.get("source_documents", [])
                        
                        # Display response
                        st.write(response_content)
                        
                        # Display sources if available
                        if sources:
                            with st.expander(f"📚 Sources ({len(sources)} references)", expanded=False):
                                for i, doc in enumerate(sources, 1):
                                    st.markdown(f"""
                                    **Source {i}:**
                                    ```
                                    {doc.page_content[:300]}...
                                    ```
                                    """)
                        
                        # Add assistant message to history
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": response_content,
                            "sources": sources
                        })
                        
                    except Exception as e:
                        error_msg = f"⚠️ I encountered an error while processing your request: {str(e)}"
                        st.error(error_msg)
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": error_msg,
                            "sources": None
                        })
            
            # Rerun to clear the input field
            st.rerun()
        
    with col2:
        st.subheader("🎯 Quick Actions")
        
        if st.button("🔄 Clear Conversation", use_container_width=True):
            st.session_state.messages = []
            st.session_state.input_text = ""  # Clear any input text
            st.rerun()
        
        st.subheader("ℹ️ About")
        st.info("""
        This chatbot uses **Retrieval-Augmented Generation (RAG)** to provide accurate, context-aware answers about cybersecurity threats.
        
        **Features:**
        - Real-time threat analysis
        - Source attribution
        - Context-aware responses
        - Conversation history
        """)
