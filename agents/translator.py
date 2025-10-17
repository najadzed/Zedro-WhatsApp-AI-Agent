import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def detect_language(text: str) -> str:
    """Detect language using OpenAI."""
    try:
        resp = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": f"Detect the language of this text in ISO code: {text}"}],
            max_tokens=10
        )
        lang = resp.choices[0].message.content.strip()
        # fallback to 'en' if something unexpected
        if not lang:
            return "en"
        return lang
    except Exception as e:
        print("⚠️ Language detection failed:", e)
        return "en"


async def translate_text(text: str, dest: str = "en") -> str:
    """Translate using OpenAI."""
    try:
        if dest.lower() == "en":
            return text  # optional: skip if already English
        resp = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": f"Translate this text to {dest}: {text}"}],
            max_tokens=500
        )
        translated = resp.choices[0].message.content.strip()
        return translated
    except Exception as e:
        print("⚠️ Translation failed:", e)
        return text
