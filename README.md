# 🛡️ Cyber Threat Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that answers questions about cybersecurity threats by analyzing PDF documents. The chatbot uses Google's Gemini model for natural language processing and FAISS for efficient vector similarity search.

## Features

- **PDF Document Processing**: Automatically loads and processes cybersecurity threat documents
- **Intelligent Question Answering**: Uses RAG to provide contextual answers based on the document content
- **Multiple Interfaces**: 
  - Streamlit web interface for interactive use
  - Command-line interface for programmatic access
- **Vector Search**: FAISS-powered similarity search for relevant document chunks
- **Source Citations**: Provides source references for transparency

## Technology Stack

- **LLM**: Google Gemini 2.0 Flash
- **Embeddings**: Google Generative AI Embeddings
- **Vector Store**: FAISS (Facebook AI Similarity Search)
- **Framework**: LangChain
- **UI**: Streamlit
- **Document Processing**: PyPDF

## Prerequisites

- Python 3.8+
- Google API Key for Gemini access

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd llm_project
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv llm_env
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     llm_env\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source llm_env/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**:
   Create a `.env` file in the project root and add your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## Usage

### Streamlit Web Interface (Recommended)

1. **Run the Streamlit app**:
   ```bash
   streamlit run main.py
   ```

2. **Access the interface**:
   Open your browser and navigate to `http://localhost:8501`

3. **Ask questions**:
   Type your cybersecurity-related questions in the input field and get AI-powered answers with source citations.

### Command Line Interface

1. **Modify the mode in `main.py`**:
   ```python
   MODE = "cli"  # Change from "streamlit" to "cli"
   ```

2. **Run the application**:
   ```bash
   python main.py
   ```

3. **Interact with the chatbot**:
   Type your questions and receive answers. Type "exit" to quit.

## Project Structure

```
llm_project/
├── main.py                 # Entry point - switches between UI modes
├── config.py              # Configuration and environment setup
├── pdf_loader.py          # PDF document loading functionality
├── text_splitter.py       # Document chunking and token counting
├── embeddings.py          # Vector embeddings and FAISS operations
├── rag_pipeline.py        # RAG chain setup with Gemini LLM
├── interface_streamlit.py # Streamlit web interface
├── interface_cli.py       # Command-line interface
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── faiss_index_cyber/     # FAISS vector store (auto-generated)
├── llm_env/              # Virtual environment (auto-generated)
└── *.pdf                 # Sample cybersecurity documents
```

## Configuration

### Changing the PDF Source

To use different PDF documents, modify the `file_path` variable in:
- `interface_streamlit.py` (line 11)
- `main.py` (line 14 for CLI mode)

### Adjusting Model Parameters

You can modify the following in `rag_pipeline.py`:
- **Model**: Change `model="gemini-2.0-flash"` to other Gemini variants
- **Temperature**: Adjust `temperature=0.5` (0.0 = deterministic, 1.0 = creative)
- **Retrieval Count**: Modify `search_kwargs={"k": 3}` to retrieve more/fewer documents

### Text Chunking Configuration

In `text_splitter.py`, adjust:
- **Chunk Size**: `chunk_size=1000` (characters per chunk)
- **Overlap**: `chunk_overlap=200` (overlap between chunks)

## Sample Questions

Try asking questions like:
- "What are the main cybersecurity threats mentioned in the document?"
- "How can organizations protect against ransomware attacks?"
- "What are the best practices for incident response?"
- "Explain the current threat landscape for financial services."

## Troubleshooting

### Common Issues

1. **Google API Key Error**:
   - Ensure your `.env` file contains a valid `GOOGLE_API_KEY`
   - Verify the API key has access to Gemini models

2. **PDF Loading Issues**:
   - Check that the PDF file exists in the project directory
   - Ensure the PDF is readable and not password-protected

3. **Memory Issues with Large PDFs**:
   - Reduce `chunk_size` in `text_splitter.py`
   - Process smaller sections of the document

4. **Slow Response Times**:
   - Reduce the number of retrieved documents (`k` parameter)
   - Use a faster Gemini model variant

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- **LangChain** for the RAG framework
- **Google AI** for Gemini language models
- **Meta AI** for FAISS vector search
- **Streamlit** for the web interface

## Future Enhancements

- [ ] Support for multiple document formats (Word, PowerPoint, etc.)
- [ ] Document upload functionality in Streamlit interface
- [ ] Conversation history and context retention
- [ ] Advanced filtering and search capabilities
- [ ] Export functionality for Q&A sessions
- [ ] Integration with more LLM providers
