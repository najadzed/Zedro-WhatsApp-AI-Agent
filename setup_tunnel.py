#!/usr/bin/env python3
"""
Setup ngrok tunnel for WhatsApp webhook testing
"""

from pyngrok import ngrok
import time
import subprocess
import sys
from pathlib import Path

def main():
    """Setup ngrok tunnel and start the chatbot server."""
    print("🚀 Setting up ngrok tunnel for WhatsApp webhook...")
    
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
    
    try:
        # Create ngrok tunnel
        print("🌐 Creating ngrok tunnel on port 8000...")
        public_url = ngrok.connect(8000)
        tunnel_url = public_url.public_url
        
        print(f"✅ Tunnel created successfully!")
        print(f"🔗 Public URL: {tunnel_url}")
        print(f"📱 WhatsApp Webhook URL: {tunnel_url}/whatsapp")
        print("-" * 60)
        print("📋 Twilio WhatsApp Configuration:")
        print(f"   Webhook URL: {tunnel_url}/whatsapp")
        print("   HTTP Method: POST")
        print("-" * 60)
        
        # Start the server
        print("📡 Starting FastAPI server...")
        uvicorn_path = venv_path / "Scripts" / "uvicorn.exe"
        
        # Run server in background
        server_process = subprocess.Popen([
            str(uvicorn_path),
            "main:app",
            "--host", "127.0.0.1",
            "--port", "8000",
            "--reload"
        ])
        
        print("✅ Server started successfully!")
        print("🛑 Press Ctrl+C to stop both server and tunnel")
        
        # Keep running until interrupted
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 Shutting down...")
            server_process.terminate()
            ngrok.disconnect(tunnel_url)
            ngrok.kill()
            print("✅ Cleanup complete")
            return 0
            
    except Exception as e:
        print(f"❌ Error setting up tunnel: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
