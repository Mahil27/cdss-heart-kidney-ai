import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def chat_with_ai(messages):
    user_msg = None

    # extract last user message safely
    for msg in reversed(messages):
        if isinstance(msg, dict):
            role = msg.get("role", "")
            content = msg.get("content", "")
        else:
            role = getattr(msg, "role", "")
            content = getattr(msg, "content", "")

        if content and role.lower() != "assistant":
            user_msg = content.strip()
            break

    if not user_msg:
        return (
            "• Health information only\n"
            "• No valid question found\n"
            "• Ask a medical question\n"
            "• Consult healthcare professional"
        )

    prompt = f"""
You are a medical assistant chatbot.

STRICT RULES:
- Answer ONLY medical or health-related questions
- If not medical, respond exactly:
  "I can only help with health-related questions."
- Use EXACTLY 4 bullet points
- Use ONLY the bullet symbol: •
- Each bullet max 8 words
- No extra explanations
- No follow-up questions

User question:
{user_msg}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=60,
            temperature=0.0,
        )
        return response.choices[0].message.content.strip()

    except Exception:
        return (
            "• Health information only\n"
            "• Unable to respond right now\n"
            "• Try again later\n"
            "• Consult healthcare professional"
        )
