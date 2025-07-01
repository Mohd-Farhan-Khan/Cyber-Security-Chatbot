from langchain.text_splitter import RecursiveCharacterTextSplitter
import tiktoken

def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=200
        )
    return splitter.split_documents(documents)

def count_tokens(text, model="gemini-pro"):
    try:
        enc = tiktoken.encoding_for_model(model)
        return len(enc.encode(text))
    except:
        return len(text.split())

def print_token_stats(chunks):
    total = 0
    for i, doc in enumerate(chunks):
        tokens = count_tokens(doc.page_content)
        print(f"Chunk {i+1}: {tokens} tokens")
        total += tokens
    print(f"Total tokens: {total}")