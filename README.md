# 🛡️ Cyber Threat Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that answers questions about cybersecurity threats by analyzing PDF documents. The chatbot uses Google's Gemini model for natural language processing and FAISS for efficient vector similarity search.

## Features

- **PDF Document Processing**: Automatically loads and processes cybersecurity threat documents
- **Intelligent Question Answering**: Uses RAG to provide contextual answers based on the document content
- **Enhanced User Interfaces**: 
  - **Streamlit Web Interface**: Modern chat-like UI with conversation history, real-time status, and interactive features
  - **Professional CLI Interface**: Rich terminal experience with animations, formatted output, and command support
- **Vector Search**: FAISS-powered similarity search for relevant document chunks
- **Source Citations**: Comprehensive source references with expandable content preview
- **Real-time Processing Feedback**: Live progress updates during document processing
- **Conversation Management**: Persistent chat history, conversation statistics, and session tracking

## User Experience Enhancements

### Streamlit Web Interface
- 🎨 **Modern Design**: Clean, professional UI with gradient headers and responsive layout
- 💬 **Chat Interface**: Real-time messaging with conversation history and typing indicators
- � **Chat Interface**: Real-time messaging with conversation history and typing indicators
- 🔧 **Interactive Controls**: Quick action buttons, sample questions, and conversation management
- 📚 **Source Explorer**: Expandable source references with full content preview

### CLI Interface
- 🎯 **Professional Banner**: ASCII art branding with system information
- ⚡ **Rich Animations**: Thinking indicators and progress feedback
- 📋 **Structured Output**: Formatted responses with numbered sources and timestamps
- 🛠️ **Command System**: Built-in help, screen clearing, and session management
- 📈 **Session Tracking**: Conversation counters and real-time statistics

## Technology Stack

- **LLM**: Google Gemini 2.0 Flash
- **Embeddings**: Google Generative AI Embeddings
- **Vector Store**: FAISS (Facebook AI Similarity Search)
- **Framework**: LangChain
- **UI**: Streamlit
- **Document Processing**: PyPDF

## 🚨 Important Security Notice
The repository contains an exposed API key that is NOT yours. You MUST replace it with your own key before running the application.

## Prerequisites

- Python 3.8+
- Google AI Studio API Key (for Gemini)

## 🔧 Step-by-Step Setup

### 1. Get Your Google API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated API key

### 2. Configure Your Environment
1. Open the `.env` file in the project root
2. Replace the existing API key with your actual API key:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

### 3. Set Up Python Environment
Open PowerShell/Command Prompt and run:

```powershell
# Navigate to the project directory
cd "c:\Users\golde\Desktop\Cyber Chatbot (Janhavi)\Cyber-Security-Chatbot"

# Create virtual environment (if not already existing)
python -m venv cyber-chatbot

# Activate virtual environment
.\cyber-chatbot\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### 4. Initialize Vector Database
Run the setup script to create a fresh vector database with your API key:

```powershell
python scripts/setup_database.py
```

This will:
- ✅ Verify your API key is configured
- 🗑️ Remove the old vector database
- 📄 Load all PDF documents
- ✂️ Split documents into chunks
- 🧠 Create new embeddings with your API key
- 💾 Save the new vector database

## Usage

### 5. Run the Chatbot

#### Option A: Web Interface (Recommended)
```powershell
streamlit run main.py
```
Then open your browser to: http://localhost:8501

#### Option B: Command Line Interface
Edit `main.py` and change:
```python
MODE = "cli"  # Change from "streamlit" to "cli"
```
Then run:
```powershell
python main.py
```

### Streamlit Web Interface Features

1. **Access the interface**:
   Open your browser and navigate to `http://localhost:8501`

2. **Interactive Chatbot Features**:
   - **Real-time conversation**: Chat-like interface with message history
   - **System status**: Live monitoring of document processing and AI system status
   - **Quick actions**: Sample questions and conversation clearing
   - **Source attribution**: Expandable source references for transparency
   - **Progress tracking**: Visual feedback during document processing
   - **Responsive design**: Clean, modern UI with professional styling

### Enhanced Command Line Interface

1. **Modify the mode in `main.py`**:
   ```python
   MODE = "cli"  # Change from "streamlit" to "cli"
   ```

2. **Run the application**:
   ```bash
   python main.py
   ```

3. **Enhanced CLI Features**:
   - **Professional banner**: ASCII art welcome screen with system branding
   - **Interactive help**: Built-in help system with sample questions
   - **Thinking animation**: Visual feedback while processing queries
   - **Formatted responses**: Clean, structured output with source attribution
   - **Session management**: Conversation tracking and timestamps
   - **Command support**: Help, clear screen, and exit commands
   - **Error handling**: Graceful error messages and recovery
   Type your questions and receive answers. Type "exit" to quit.

## Project Structure

```
Cyber-Security-Chatbot/
├── main.py                      # Entry point - switches between UI modes
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables
├── .gitignore                   # Git ignore file
├── README.md                    # Project documentation
├── src/                         # Source code package
│   ├── __init__.py             # Package initialization
│   ├── config.py               # Configuration and environment setup
│   ├── pdf_loader.py           # PDF document loading functionality
│   ├── text_splitter.py        # Document chunking
│   ├── embeddings.py           # Vector embeddings and FAISS operations
│   ├── rag_pipeline.py         # RAG chain setup with Gemini LLM
│   └── interfaces/             # User interface modules
│       ├── __init__.py         # Interface package initialization
│       ├── streamlit_app.py    # Streamlit web interface
│       └── cli_app.py          # Command-line interface
├── scripts/                     # Utility scripts
│   ├── __init__.py             # Scripts package initialization
│   └── setup_database.py       # Database setup and initialization script
├── data/                        # PDF documents directory
│   ├── financial_services_cyber_threats_dataset.pdf
│   ├── Cyber Threat Sample.pdf
│   └── Cyber Threat Sample1.pdf
├── faiss_index_cyber/          # FAISS vector store (auto-generated)
│   ├── index.faiss             # FAISS index file
│   └── index.pkl               # Serialized index metadata
├── cyber-chatbot/              # Virtual environment (auto-generated)
│   ├── pyvenv.cfg              # Virtual environment configuration
│   ├── Scripts/                # Virtual environment executables
│   ├── Lib/                    # Virtual environment libraries
│   └── Include/                # Virtual environment headers
└── __pycache__/                # Python cache files (auto-generated)
```

## Configuration

### Changing the PDF Source

To use different PDF documents, modify the file paths in:
- `main.py` (line 14 for CLI mode)
- `src/interfaces/streamlit_app.py` (for Streamlit interface)
- `scripts/setup_database.py` (for database setup)

### Adjusting Model Parameters

You can modify the following in `src/rag_pipeline.py`:
- **Model**: Change `model="gemini-2.0-flash"` to other Gemini variants
- **Temperature**: Adjust `temperature=0.5` (0.0 = deterministic, 1.0 = creative)
- **Retrieval Count**: Modify `search_kwargs={"k": 3}` to retrieve more/fewer documents

### Text Chunking Configuration

In `src/text_splitter.py`, adjust:
- **Chunk Size**: `chunk_size=1000` (characters per chunk)
- **Overlap**: `chunk_overlap=200` (overlap between chunks)

## Sample Questions

Try asking questions like:
- "What are the main cybersecurity threats mentioned in the document?"
- "How can organizations protect against ransomware attacks?"
- "What are the best practices for incident response?"
- "Explain the current threat landscape for financial services."

## 🔍 Troubleshooting

### Common Issues

1. **Google API Key Error**:
   - Ensure your `.env` file contains a valid `GOOGLE_API_KEY`
   - Verify the API key has access to Gemini models
   - Make sure your API key is correctly set in `.env`

2. **PDF Loading Issues**:
   - Check that the PDF file exists in the project directory
   - Ensure the PDF is readable and not password-protected

3. **Memory Issues with Large PDFs**:
   - Reduce `chunk_size` in `text_splitter.py`
   - Process smaller sections of the document

4. **Slow Response Times**:
   - Reduce the number of retrieved documents (`k` parameter)
   - Use a faster Gemini model variant

5. **Module Not Found**: 
   - Ensure you've activated the virtual environment and installed requirements

6. **Permission Errors**: 
   - Run PowerShell as Administrator if needed

7. **FAISS Index Error**: 
   - Delete the `faiss_index_cyber` folder and run `python scripts/setup_database.py` again

### PowerShell Execution Policy
If you get execution policy errors, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 📊 What Documents Are Included?
The chatbot will process these PDF files from the `data/` directory:
- `data/financial_services_cyber_threats_dataset.pdf`
- `data/Cyber Threat Sample.pdf`
- `data/Cyber Threat Sample1.pdf`

## 🛡️ Security Best Practices
- ✅ Never share your API key
- ✅ Add `.env` to `.gitignore` if contributing
- ✅ Use environment variables for sensitive data
- ✅ Regularly rotate API keys

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

## Recently Implemented

- ✅ **Enhanced Chat Interface**: Real-time conversation with message history
- ✅ **System Status Dashboard**: Live monitoring and document information
- ✅ **Professional CLI Experience**: Rich terminal interface with animations
- ✅ **Interactive Quick Actions**: Sample questions and conversation management
- ✅ **Source Attribution System**: Expandable references with content preview
- ✅ **Session Management**: Conversation tracking and statistics

## Future Enhancements

- [ ] Support for multiple document formats (Word, PowerPoint, etc.)
- [ ] Document upload functionality in Streamlit interface
- [ ] Advanced filtering and search capabilities
- [ ] Export functionality for Q&A sessions
- [ ] Integration with more LLM providers
- [ ] Multi-language support
- [ ] Custom theme options
