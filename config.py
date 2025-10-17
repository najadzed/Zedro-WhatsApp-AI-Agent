from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

# --- Common variables ---
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER")

# --- Model keys ---
USE_GEMINI = os.getenv("USE_GEMINI", "true").lower() == "true"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# --- Validation ---
if USE_GEMINI:
    if not GEMINI_API_KEY:
        raise ValueError("❌ Missing GEMINI_API_KEY but USE_GEMINI=true in .env")
else:
    if not OPENAI_API_KEY:
        raise ValueError("❌ Missing OPENAI_API_KEY but USE_GEMINI=false in .env")
