
# main.py
from dotenv import load_dotenv
import os

load_dotenv()  # <-- this loads the .env file into os.environ

from fastapi import FastAPI
from routes.whatsapp import router as whatsapp_router

app = FastAPI(title="Zedro - WhatsApp AI Agent")
app.include_router(whatsapp_router)

@app.get("/")
def root():
    return {"message": "🚀 Zedro AI backend is running successfully!"}
