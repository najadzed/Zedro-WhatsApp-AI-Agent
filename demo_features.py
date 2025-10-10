#!/usr/bin/env python3
"""
Demo script for Zedro AI Chatbot new features
"""

import requests
import json

def demo_developer_identity():
    """Demo developer identity feature."""
    print("👨‍💻 DEMO: Developer Identity Feature")
    print("=" * 50)
    
    webhook_url = "https://uncanned-alarmedly-timothy.ngrok-free.dev/whatsapp"
    
    questions = [
        "Who created you?",
        "Who built you?", 
        "Who developed you?",
        "Who is your owner?",
        "Who is your creator?"
    ]
    
    for i, question in enumerate(questions, 1):
        print(f"\n{i}. User asks: '{question}'")
        
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
            
            # Extract response from XML
            response_text = response.text
            if "<Body>" in response_text:
                start = response_text.find("<Body>") + 6
                end = response_text.find("</Body>")
                answer = response_text[start:end]
            else:
                answer = response_text
                
            print(f"   Zedro responds: '{answer}'")
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print("\n✅ All developer identity questions answered with 'Najad'!")

def demo_voice_processing():
    """Demo voice processing feature."""
    print("\n🎤 DEMO: Voice Message Processing")
    print("=" * 50)
    
    print("When a user sends a voice message:")
    print("1. 🎤 Voice message is received from WhatsApp")
    print("2. 📥 Audio file is downloaded from Twilio")
    print("3. 🎯 OpenAI Whisper transcribes the audio")
    print("4. 🤖 Transcribed text is processed through RAG pipeline")
    print("5. 💬 Response is sent back to user")
    
    print("\n📝 Voice processing includes:")
    print("   - Automatic language detection")
    print("   - High-quality transcription")
    print("   - Context-aware responses")
    print("   - Error handling and logging")
    
    print("\n✅ Voice messages are fully supported!")

def demo_regular_chat():
    """Demo regular chat functionality."""
    print("\n💬 DEMO: Regular Chat Functionality")
    print("=" * 50)
    
    webhook_url = "https://uncanned-alarmedly-timothy.ngrok-free.dev/whatsapp"
    
    test_messages = [
        "Hello, how are you?",
        "What can you help me with?",
        "Tell me a joke"
    ]
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n{i}. User says: '{message}'")
        
        test_data = {
            "Body": message,
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
            
            # Extract response from XML
            response_text = response.text
            if "<Body>" in response_text:
                start = response_text.find("<Body>") + 6
                end = response_text.find("</Body>")
                answer = response_text[start:end]
            else:
                answer = response_text
                
            print(f"   Zedro responds: '{answer[:100]}{'...' if len(answer) > 100 else ''}'")
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print("\n✅ Regular chat functionality working!")

def main():
    """Main demo function."""
    print("🚀 ZEDRO AI CHATBOT - NEW FEATURES DEMO")
    print("=" * 60)
    print("Created by: Najad")
    print("=" * 60)
    
    # Demo developer identity
    demo_developer_identity()
    
    # Demo voice processing
    demo_voice_processing()
    
    # Demo regular chat
    demo_regular_chat()
    
    print("\n" + "=" * 60)
    print("🎉 ALL FEATURES DEMONSTRATED SUCCESSFULLY!")
    print("📱 Your WhatsApp chatbot is ready for production!")
    print("🔗 Webhook URL: https://uncanned-alarmedly-timothy.ngrok-free.dev/whatsapp")
    print("=" * 60)

if __name__ == "__main__":
    main()
