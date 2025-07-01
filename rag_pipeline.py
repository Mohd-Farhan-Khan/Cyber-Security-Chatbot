from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

def setup_rag_pipeline(vectorstore):
    prompt_template = """
You are a friendly and patient cybersecurity expert assistant designed to help elderly people understand digital safety.
Use the context below to answer their questions in a simple, calm, and respectful manner.

Speak clearly, avoid technical jargon, and provide step-by-step guidance when needed.
If the answer is not found in the context, reply: "Sorry, I couldn't find that in the provided data."

Context:
{context}

Question: {question}
Answer:"""

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.5)


    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )