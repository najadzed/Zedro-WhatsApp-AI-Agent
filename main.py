# main.py
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.whatsapp import router as whatsapp_router

# ✅ Load environment variables
load_dotenv()

# ✅ Initialize app
app = FastAPI(title="Zedro - WhatsApp AI Agent")

# ✅ Include WhatsApp routes
app.include_router(whatsapp_router)

# ✅ Serve generated images from /data folder
# This allows Twilio to access generated image URLs like:
# https://your-app.onrender.com/static/generated_image.jpg
if not os.path.exists("data"):
    os.makedirs("data")

app.mount("/static", StaticFiles(directory="data"), name="static")

@app.get("/")
def root():
    return {"message": "🚀 Zedro AI backend is running successfully with image generation support!"}
