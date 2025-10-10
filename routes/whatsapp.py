from fastapi import APIRouter, Request, Response
from twilio.twiml.messaging_response import MessagingResponse
from agents.rag_agent import rag_pipeline
from agents.voice_handler import handle_voice_note

router = APIRouter()

@router.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    form = await request.form()
    incoming_msg = form.get("Body", "")
    if isinstance(incoming_msg, dict):
        incoming_msg = incoming_msg.get("text", "")
    incoming_msg = str(incoming_msg)

    msg_type = (form.get("MessageType", "") or "").lower()
    media_url = form.get("MediaUrl0", "")

    resp = MessagingResponse()
    msg = resp.message()

    try:
        # Voice note
        if msg_type == "voice" and media_url:
            print(f"🎤 Processing voice message from: {form.get('From', 'Unknown')}")
            transcribed_text = await handle_voice_note(media_url)
            print(f"📝 Transcribed text: {transcribed_text}")
            
            # Process transcribed text through RAG pipeline
            result = rag_pipeline.invoke({"query": transcribed_text})
            
            if hasattr(result, "content"):
                answer_text = str(result.content)
            elif isinstance(result, dict):
                answer_text = str(result.get("content") or result.get("answer") or result)
            else:
                answer_text = str(result)
                
            print(f"🤖 Voice response: {answer_text}")
        else:
            # Text message - check for developer identity questions first
            incoming_msg_lower = incoming_msg.lower()
            developer_keywords = ["who created you", "who built you", "who developed you", "who is your owner", 
                                "who is your creator", "who made you", "who designed you", "developer", "owner"]
            
            if any(keyword in incoming_msg_lower for keyword in developer_keywords):
                answer_text = "I was created by Najad. He is my developer and the one who built me. I'm Zedro, his AI assistant!"
                print(f"👨‍💻 Developer identity response: {answer_text}")
            else:
                # Regular text message through RAG pipeline
                result = rag_pipeline.invoke({"query": incoming_msg})

                if hasattr(result, "content"):
                    answer_text = str(result.content)
                elif isinstance(result, dict):
                    answer_text = str(result.get("content") or result.get("answer") or result)
                else:
                    answer_text = str(result)

        msg.body(answer_text)

    except Exception as e:
        print("❌ Error while processing WhatsApp message:", e)
        msg.body(f"⚠️ Something went wrong: {e}")

    return Response(content=str(resp), media_type="application/xml")
