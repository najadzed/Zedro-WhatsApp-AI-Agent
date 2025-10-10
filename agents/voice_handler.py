import aiohttp
import tempfile
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

async def handle_voice_note(media_url: str) -> str:
    """Download voice note from Twilio, transcribe with Gemini 1.5"""
    try:
        print(f"🎤 Downloading voice note from: {media_url}")
        
        async with aiohttp.ClientSession() as session:
            async with session.get(media_url) as resp:
                if resp.status != 200:
                    print(f"❌ Failed to download voice note. Status: {resp.status}")
                    return "⚠️ Failed to fetch voice note"
                data = await resp.read()
                print(f"📥 Downloaded {len(data)} bytes of audio data")

        # Save temporarily as mp3
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            f.write(data)
            tmp_file = f.name
            print(f"💾 Saved audio to temporary file: {tmp_file}")

        # Transcribe using Gemini 1.5
        print("🎯 Starting transcription with Gemini 1.5...")
        model = genai.GenerativeModel("gemini-1.5-pro")
        with open(tmp_file, "rb") as f:
            audio = {"mime_type": "audio/mp3", "data": f.read()}
        response = model.generate_content([
            audio,
            {"text": "Transcribe this audio. Detect and use the spoken language."}
        ])
        
        # Clean up temporary file
        import os
        try:
            os.unlink(tmp_file)
            print(f"🗑️ Cleaned up temporary file: {tmp_file}")
        except:
            pass
            
        text = getattr(response, "text", None) or getattr(response, "candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
        print(f"✅ Transcription completed: {text}")
        return text or ""
        
    except Exception as e:
        print(f"❌ Error processing voice note: {e}")
        return f"⚠️ Error processing voice message: {str(e)}"
