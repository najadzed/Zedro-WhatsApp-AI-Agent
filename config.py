from dotenv import load_dotenv
import os

# Load all variables from .env
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER")

# Validate critical keys
if not GEMINI_API_KEY:
    raise ValueError("❌ Missing GEMINI_API_KEY in .env file")
