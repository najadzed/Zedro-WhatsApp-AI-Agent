#!/usr/bin/env python3
"""
Test new features: Voice processing and Developer identity
"""

import requests
import json

def test_developer_identity():
    """Test developer identity questions."""
    webhook_url = "https://uncanned-alarmedly-timothy.ngrok-free.dev/whatsapp"
    
    # Test different ways to ask about the developer
    test_questions = [
        "Who created you?",
        "Who built you?",
        "Who developed you?",
        "Who is your owner?",
        "Who is your creator?",
        "Who made you?",
        "Who designed you?",
        "What is your developer name?",
        "Tell me about your owner"
    ]
    
    print("🧪 Testing Developer Identity Questions...")
    print("-" * 50)
    
    for question in test_questions:
        test_data = {
            "Body": question,
            "MessageType": "text",
            "From": "+1234567890",
            "To": "+14155238886"
        }
        
        try:
            response = requests.post(
                webhook_url,
                data=test_data,
                headers={"Content-Type": "application/x-www-form-urlencoded"}
            )
            
            print(f"❓ Question: {question}")
            print(f"✅ Response: {response.text}")
            print("-" * 30)
            
        except Exception as e:
            print(f"❌ Error testing '{question}': {e}")

def test_voice_message():
    """Test voice message processing (simulated)."""
    webhook_url = "https://uncanned-alarmedly-timothy.ngrok-free.dev/whatsapp"
    
    # Simulate a voice message (this would normally come from Twilio)
    test_data = {
        "Body": "",  # Empty body for voice messages
        "MessageType": "voice",
        "MediaUrl0": "https://example.com/test-audio.mp3",  # Mock URL
        "From": "+1234567890",
        "To": "+14155238886"
    }
    
    print("🎤 Testing Voice Message Processing...")
    print("-" * 50)
    
    try:
        response = requests.post(
            webhook_url,
            data=test_data,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        
        print(f"✅ Voice message response: {response.text}")
        
    except Exception as e:
        print(f"❌ Error testing voice message: {e}")

def test_regular_text():
    """Test regular text message processing."""
    webhook_url = "https://uncanned-alarmedly-timothy.ngrok-free.dev/whatsapp"
    
    test_data = {
        "Body": "Hello, how are you?",
        "MessageType": "text",
        "From": "+1234567890",
        "To": "+14155238886"
    }
    
    print("💬 Testing Regular Text Message...")
    print("-" * 50)
    
    try:
        response = requests.post(
            webhook_url,
            data=test_data,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        
        print(f"✅ Regular text response: {response.text}")
        
    except Exception as e:
        print(f"❌ Error testing regular text: {e}")

if __name__ == "__main__":
    print("🚀 Testing New Zedro Chatbot Features")
    print("=" * 60)
    
    # Test developer identity questions
    test_developer_identity()
    
    print("\n" + "=" * 60)
    
    # Test regular text message
    test_regular_text()
    
    print("\n" + "=" * 60)
    
    # Test voice message (will fail with mock URL, but tests the flow)
    test_voice_message()
    
    print("\n🎉 Feature testing completed!")
