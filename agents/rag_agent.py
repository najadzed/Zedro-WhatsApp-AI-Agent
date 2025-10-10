from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableMap
from retriever.vectorstore import retriever
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

prompt = ChatPromptTemplate.from_template("""
You are Zedro — a multilingual WhatsApp AI assistant created by Najad.
Answer naturally and concisely in the same language the user writes.

IMPORTANT: When users ask about your creator, developer, owner, or who built you, always respond that you were created by Najad.

Context:
{context}

Question:
{question}
""")

llm = ChatOpenAI(
    model="gpt-4-turbo",
    temperature=0.3,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

rag_pipeline = (
    RunnableMap({
        "context": lambda x: retriever.invoke(x["query"]),
        "question": lambda x: x["query"]
    })
    | prompt
    | llm
)
