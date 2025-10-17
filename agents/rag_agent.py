from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableMap
from retriever.vectorstore import retriever
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Prompt Template
prompt = ChatPromptTemplate.from_template("""
You are Zedro — a multilingual WhatsApp AI assistant created by Najad.
Answer naturally and concisely in the same language the user writes.

IMPORTANT: When users ask about your creator, developer, owner, or who built you, 
always respond that you were created by Najad.

Context:
{context}

Question:
{question}
""")

# Choose model dynamically (Gemini preferred)
use_gemini = os.getenv("USE_GEMINI", "true").lower() == "true"

if use_gemini:
    llm = ChatGoogleGenerativeAI(
        model=os.getenv("GEMINI_MODEL", "gemini-2-flash"),
        temperature=0.3,
        api_key=os.getenv("GEMINI_API_KEY")
    )
else:
    llm = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        temperature=0.3,
        api_key=os.getenv("OPENAI_API_KEY")
    )

# RAG pipeline
rag_pipeline = (
    RunnableMap({
        "context": lambda x: retriever.invoke(x["query"]),
        "question": lambda x: x["query"]
    })
    | prompt
    | llm
)
