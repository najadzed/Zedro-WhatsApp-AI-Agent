#!/usr/bin/env python3
"""
Zedro AI Chatbot Startup Script
This script starts the WhatsApp AI chatbot server.
"""

import subprocess
import sys
import os
from pathlib import Path

def main():
    """Start the Zedro AI chatbot server."""
    print("🚀 Starting Zedro AI Chatbot...")
    
    # Check if virtual environment exists
    venv_path = Path("zed_env")
    if not venv_path.exists():
        print("❌ Virtual environment not found. Please run setup first.")
        return 1
    
    # Check if .env file exists
    env_path = Path(".env")
    if not env_path.exists():
        print("❌ .env file not found. Please create one with your API keys.")
        return 1
    
    # Start the server
    try:
        print("📡 Starting FastAPI server on http://127.0.0.1:8000")
        print("📚 API documentation available at http://127.0.0.1:8000/docs")
        print("🛑 Press Ctrl+C to stop the server")
        print("-" * 50)
        
        # Use the virtual environment's uvicorn
        uvicorn_path = venv_path / "Scripts" / "uvicorn.exe"
        subprocess.run([
            str(uvicorn_path),
            "main:app",
            "--host", "127.0.0.1",
            "--port", "8000",
            "--reload"
        ])
        
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
        return 0
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
