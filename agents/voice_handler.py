import aiohttp
import tempfile
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def handle_voice_note(media_url: str) -> str:
    """Download voice note from Twilio, transcribe with OpenAI Whisper"""
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

        # Transcribe using OpenAI Whisper
        print("🎯 Starting transcription with OpenAI Whisper...")
        audio_file = open(tmp_file, "rb")
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language="auto"  # Auto-detect language
        )
        audio_file.close()
        
        # Clean up temporary file
        import os
        try:
            os.unlink(tmp_file)
            print(f"🗑️ Cleaned up temporary file: {tmp_file}")
        except:
            pass
            
        print(f"✅ Transcription completed: {transcription.text}")
        return transcription.text
        
    except Exception as e:
        print(f"❌ Error processing voice note: {e}")
        return f"⚠️ Error processing voice message: {str(e)}"
