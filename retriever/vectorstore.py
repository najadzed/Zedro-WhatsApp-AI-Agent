# retriever/vectorstore.py
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Make sure your OPENAI_API_KEY is set in .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI embeddings
embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# Initialize Chroma vector store
db = Chroma(
    persist_directory="./data/embeddings",  # where embeddings are stored
    embedding_function=embedding
)

# Optional: simple retriever to use in your RAG pipeline
retriever = db.as_retriever(search_kwargs={"k": 3})
