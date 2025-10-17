from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

USE_GEMINI = os.getenv("USE_GEMINI", "true").lower() == "true"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# --- Choose embedding model dynamically ---
if USE_GEMINI:
    print("🧠 Using Gemini embeddings (text-embedding-004)")
    embedding = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        google_api_key=GEMINI_API_KEY
    )
else:
    print("🧠 Using OpenAI embeddings (text-embedding-3-large)")
    embedding = OpenAIEmbeddings(
        model="text-embedding-3-large",
        api_key=OPENAI_API_KEY
    )

# --- Initialize Chroma vector store ---
db = Chroma(
    persist_directory="./data/embeddings",
    embedding_function=embedding
)

# --- Retriever for RAG pipeline ---
retriever = db.as_retriever(search_kwargs={"k": 3})
