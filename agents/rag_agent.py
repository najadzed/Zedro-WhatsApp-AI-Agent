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

# --- Primary: Gemini ---
try:
    print("🚀 Using Gemini model...")
    llm = ChatGoogleGenerativeAI(
        model=os.getenv("GEMINI_MODEL", "gemini-1.5-flash"),
        temperature=0.3,
        api_key=os.getenv("GEMINI_API_KEY")
    )
    # If initialization succeeds:
    print("✅ Gemini initialized successfully.")

except Exception as e:
    print(f"⚠️ Gemini initialization failed: {e}")
    print("🔁 Switching to OpenAI fallback...")
    llm = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        temperature=0.3,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    print("✅ OpenAI fallback active.")

# --- Build RAG pipeline ---
rag_pipeline = (
    RunnableMap({
        "context": lambda x: retriever.invoke(x["query"]),
        "question": lambda x: x["query"]
    })
    | prompt
    | llm
)
