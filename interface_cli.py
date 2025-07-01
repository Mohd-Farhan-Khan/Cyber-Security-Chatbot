def run_chatbot_cli(qa_chain):
    print("Cyber Threat Chatbot (CLI)")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        result = qa_chain({"query": query})
        print("Answer:", result["result"])
        print("Sources:")
        for doc in result["source_documents"]:
            print("-", doc.page_content[:100])