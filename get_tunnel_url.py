
#!/usr/bin/env python3
"""
Get ngrok tunnel URL for WhatsApp webhook
"""

import requests
import json
import time
import subprocess
import sys
from pathlib import Path

def start_ngrok():
    """Start ngrok tunnel."""
    print("🌐 Starting ngrok tunnel...")
    venv_path = Path("zed_env")
    ngrok_path = venv_path / "Scripts" / "ngrok.exe"
    
    # Start ngrok in background
    subprocess.Popen([
        str(ngrok_path),
        "http", "8000",
        "--log=stdout"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Wait for ngrok to start
    time.sleep(3)

def get_tunnel_url():
    """Get the tunnel URL from ngrok API."""
    try:
        response = requests.get("http://localhost:4040/api/tunnels")
        data = response.json()
        
        tunnels = data.get("tunnels", [])
        if tunnels:
            public_url = tunnels[0]["public_url"]
            webhook_url = public_url + "/whatsapp"
            
            print("✅ Tunnel created successfully!")
            print(f"🔗 Public URL: {public_url}")
            print(f"📱 WhatsApp Webhook URL: {webhook_url}")
            print("-" * 60)
            print("📋 Twilio WhatsApp Configuration:")
            print(f"   Webhook URL: {webhook_url}")
            print("   HTTP Method: POST")
            print("-" * 60)
            
            return webhook_url
        else:
            print("❌ No tunnels found")
            return None
            
    except Exception as e:
        print(f"❌ Error getting tunnel URL: {e}")
        return None

def main():
    """Main function."""
    print("🚀 Setting up ngrok tunnel for WhatsApp webhook...")
    
    # Check if virtual environment exists
    venv_path = Path("zed_env")
    if not venv_path.exists():
        print("❌ Virtual environment not found.")
        return 1
    
    # Start ngrok
    start_ngrok()
    
    # Get tunnel URL
    webhook_url = get_tunnel_url()
    
    if webhook_url:
        print("\n🎉 Ready for Twilio configuration!")
        print("📝 Copy the webhook URL above to your Twilio WhatsApp sandbox settings.")
        return 0
    else:
        print("❌ Failed to create tunnel")
        return 1

if __name__ == "__main__":
    sys.exit(main())
