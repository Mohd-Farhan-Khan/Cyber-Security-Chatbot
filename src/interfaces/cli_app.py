import os
import time
from datetime import datetime

def print_banner():
    """Print a nice banner for the chatbot"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║    🛡️  CYBER THREAT INTELLIGENCE CHATBOT  🛡️                ║
║                                                              ║
║    Your AI-powered cybersecurity analyst                    ║
║    Powered by Google Gemini & RAG Technology                ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(banner)

def print_help():
    """Print help information"""
    help_text = """
┌─ 💡 SAMPLE QUESTIONS ─────────────────────────────────────────┐
│                                                              │
│ • What are the main cybersecurity threats?                  │
│ • How can organizations protect against ransomware?         │
│ • What are the best practices for incident response?        │
│ • Explain the current threat landscape                      │
│ • What security measures are recommended?                   │
│                                                              │
└──────────────────────────────────────────────────────────────┘

Commands:
  help    - Show this help message
  clear   - Clear the screen
  exit    - Exit the chatbot
"""
    print(help_text)

def print_thinking():
    """Show a thinking animation"""
    thinking_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    print("🤖 Assistant: ", end="", flush=True)
    for i in range(10):
        print(f"\r🤖 Assistant: {thinking_chars[i % len(thinking_chars)]} Analyzing threat intelligence...", end="", flush=True)
        time.sleep(0.1)
    print("\r🤖 Assistant: ", end="", flush=True)

def format_response(result):
    """Format the AI response nicely"""
    response = result["result"]
    sources = result.get("source_documents", [])
    
    # Print main response
    print(f"{response}\n")
    
    # Print sources if available
    if sources:
        print(f"📚 Sources ({len(sources)} references):")
        print("─" * 60)
        for i, doc in enumerate(sources, 1):
            content = doc.page_content[:200].strip()
            print(f"[{i}] {content}...")
            print()

def run_chatbot_cli(qa_chain):
    """Run the enhanced CLI chatbot interface"""
    # Clear screen and show banner
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    
    # Show system status
    print("📊 System Status:")
    print("   ✅ Documents loaded and processed")
    print("   ✅ Vector embeddings created")
    print("   ✅ RAG pipeline ready")
    print(f"   📅 Session started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Welcome message
    welcome_msg = """🤖 Assistant: Hello! I'm your Cyber Threat Intelligence assistant. I've analyzed 
cybersecurity documents and I'm ready to answer your questions about threats, 
vulnerabilities, and security best practices.

Type 'help' for sample questions or 'exit' to quit.
"""
    print(welcome_msg)
    print("─" * 70)
    
    conversation_count = 0
    
    while True:
        try:
            # Get user input
            query = input("\n👤 You: ").strip()
            
            if not query:
                continue
                
            # Handle commands
            if query.lower() == "exit":
                print("\n🤖 Assistant: Goodbye! Stay secure! 🛡️")
                break
            elif query.lower() == "help":
                print_help()
                continue
            elif query.lower() == "clear":
                os.system('cls' if os.name == 'nt' else 'clear')
                print_banner()
                continue
            
            # Process query
            print_thinking()
            
            try:
                result = qa_chain.invoke({"query": query})
                conversation_count += 1
                
                # Format and display response
                format_response(result)
                
                # Show conversation stats
                print(f"📈 Conversation #{conversation_count} | {datetime.now().strftime('%H:%M:%S')}")
                print("─" * 70)
                
            except Exception as e:
                print(f"\n⚠️  Error processing your request: {str(e)}")
                print("Please try rephrasing your question or contact support.\n")
                print("─" * 70)
                
        except KeyboardInterrupt:
            print("\n\n🤖 Assistant: Session interrupted. Goodbye! 🛡️")
            break
        except EOFError:
            print("\n\n🤖 Assistant: Session ended. Goodbye! 🛡️")
            break
