from fastapi import APIRouter, Request, Response
from twilio.twiml.messaging_response import MessagingResponse
from agents.rag_agent import rag_pipeline
from agents.voice_handler import handle_voice_note
from agents.image_generator import generate_image  # ✅ new import
import os

router = APIRouter()

@router.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    form = await request.form()
    incoming_msg = form.get("Body", "")
    if isinstance(incoming_msg, dict):
        incoming_msg = incoming_msg.get("text", "")
    incoming_msg = str(incoming_msg).strip().lower()

    msg_type = (form.get("MessageType", "") or "").lower()
    media_url = form.get("MediaUrl0", "")

    resp = MessagingResponse()
    msg = resp.message()

    try:
        # 🎤 Voice messages
        if msg_type == "voice" and media_url:
            transcribed_text = await handle_voice_note(media_url)
            result = rag_pipeline.invoke({"query": transcribed_text})
            answer_text = getattr(result, "content", str(result))
            msg.body(answer_text)

        # 🖼️ Image generation
        elif incoming_msg.startswith("generate image") or incoming_msg.startswith("draw") or incoming_msg.startswith("create image"):
            prompt = incoming_msg.replace("generate image", "").replace("draw", "").replace("create image", "").strip()
            if not prompt:
                msg.body("Please describe the image you'd like me to create 😊")
            else:
                image_path = generate_image(prompt)
                if image_path and os.path.exists(image_path):
                    msg.body(f"Here's your image for: {prompt}")
                    msg.media(f"https://your-render-domain.com/static/{os.path.basename(image_path)}")  # ✅ serve via static route
                else:
                    msg.body("⚠️ Sorry, I couldn’t generate the image. Please try again.")

        # 💬 Text messages
        else:
            result = rag_pipeline.invoke({"query": incoming_msg})
            answer_text = getattr(result, "content", str(result))
            msg.body(answer_text)

    except Exception as e:
        print("❌ Error while processing WhatsApp message:", e)
        msg.body(f"⚠️ Something went wrong: {e}")

    return Response(content=str(resp), media_type="application/xml")
