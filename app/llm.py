import os
from groq import Groq

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None


def generate_explanation(disease, prediction, probability, risk, input_data):
    prompt = f"""
You are a medical assistant.

STRICT RULES:
- EXACTLY 4 bullet points
- Use ONLY the bullet symbol: •
- Each bullet max 8 words
- No extra text

Disease: {disease}
Risk: {risk}
Probability: {probability:.2f}

Bullets order:
1 Meaning
2 Risk level
3 Lifestyle advice
4 Disclaimer
"""

    if not client:
        return (
            "• Risk estimated by ML model\n"
            "• Risk level requires attention\n"
            "• Maintain healthy lifestyle habits\n"
            "• Consult a medical professional"
        )

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
            "• Risk estimated by ML model\n"
            "• Follow healthy habits\n"
            "• Monitor health regularly\n"
            "• Consult a medical professional"
        )
