# retriever/vectorstore.py
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Make sure your GEMINI_API_KEY is set in .env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini embeddings
embedding = GoogleGenerativeAIEmbeddings(
    model="text-embedding-004",
    google_api_key=GEMINI_API_KEY
)

# Initialize Chroma vector store
db = Chroma(
    persist_directory="./data/embeddings",  # where embeddings are stored
    embedding_function=embedding
)

# Optional: simple retriever to use in your RAG pipeline
retriever = db.as_retriever(search_kwargs={"k": 3})
