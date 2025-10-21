import os
import google.generativeai as genai
from PIL import Image
import requests
from io import BytesIO

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 🖼️ Text → Image
def generate_image(prompt: str) -> str:
    """Generate an image using Imagen 4.0"""
    try:
        model = genai.GenerativeModel("models/imagen-4.0-generate-001")
        response = model.generate_content([prompt], generation_config={"response_mime_type": "image/png"})

        # Save image
        image_data = response.parts[0].data
        os.makedirs("data", exist_ok=True)
        file_path = "data/generated_image.png"
        with open(file_path, "wb") as f:
            f.write(image_data)

        print(f"✅ Image generated: {file_path}")
        return "/static/generated_image.png"
    except Exception as e:
        print(f"❌ Imagen generation failed: {e}")
        return None


# 👁️ Image → Text or Image + Text
def analyze_image(image_url: str, user_prompt: str = "Describe this image.") -> str:
    """Analyze an image using Gemini 2.5 Flash"""
    try:
        img_response = requests.get(image_url)
        image = Image.open(BytesIO(img_response.content))

        model = genai.GenerativeModel("models/gemini-2.5-flash")
        response = model.generate_content([user_prompt, image])

        result = response.text
        print(f"🧠 Visual analysis result: {result}")
        return result
    except Exception as e:
        print(f"❌ Gemini visual analysis failed: {e}")
        return "⚠️ Sorry, I couldn’t process the image."
