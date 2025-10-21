import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_image(prompt: str, output_path: str = "./data/generated_image.jpg") -> str:
    """
    Generate an image using Gemini's Imagen model.
    Returns the path to the saved image file.
    """
    try:
        model = genai.GenerativeModel("models/imagen-4.0-generate-001")  # ✅ latest Imagen model
        result = model.generate_images(prompt=prompt)

        # Save first generated image
        if result.generated_images:
            image_bytes = result.generated_images[0]._image_bytes
            with open(output_path, "wb") as f:
                f.write(image_bytes)
            print(f"🖼️ Image saved to {output_path}")
            return output_path
        else:
            print("⚠️ No image generated")
            return None

    except Exception as e:
        print(f"❌ Image generation failed: {e}")
        return None
