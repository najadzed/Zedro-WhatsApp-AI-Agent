#!/usr/bin/env python3
"""
Test WhatsApp webhook endpoint
"""

import requests
import json

def test_webhook():
    """Test the WhatsApp webhook endpoint."""
    webhook_url = "https://uncanned-alarmedly-timothy.ngrok-free.dev/whatsapp"
    
    # Test data simulating Twilio webhook
    test_data = {
        "Body": "Hello, this is a test message",
        "MessageType": "text",
        "From": "+1234567890",
        "To": "+14155238886"
    }
    
    print("🧪 Testing WhatsApp webhook...")
    print(f"📡 URL: {webhook_url}")
    print(f"📝 Test message: {test_data['Body']}")
    print("-" * 50)
    
    try:
        response = requests.post(
            webhook_url,
            data=test_data,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        
        print(f"✅ Status Code: {response.status_code}")
        print(f"📄 Response: {response.text}")
        
        if response.status_code == 200:
            print("🎉 Webhook test successful!")
            return True
        else:
            print("❌ Webhook test failed!")
            return False
            
    except Exception as e:
        print(f"❌ Error testing webhook: {e}")
        return False

if __name__ == "__main__":
    test_webhook()
