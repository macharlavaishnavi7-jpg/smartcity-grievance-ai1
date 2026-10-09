
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


def generate_guidance(question: str, guidance_context: str) -> str:
    """
    Generate informational civic guidance using Gemini.
    The chatbot must not register complaints or promise resolutions.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    model = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY is missing. Add it to your local .env file."
        )

    client = genai.Client(api_key=api_key)

    prompt = f"""
You are a Smart City Grievance Guide.

Your role is to explain civic grievance categories, general procedures,
and where citizens can find official guidance.

Rules:
- Do not register, submit, or file complaints.
- Do not track complaint status.
- Never guarantee or promise a resolution or timeline.
- Do not invent official procedures or deadlines.
- Clearly explain when citizens should consult the relevant official authority.
- Use simple, respectful language.

Available civic guidance:
{guidance_context}

Citizen's question:
{question}

Provide a concise, informational answer.
"""

    response = client.models.generate_content(
        model=model,
        contents=prompt,
    )

    answer = response.text
    if not answer:
        return (
            "I couldn't generate guidance right now. Please consult "
            "the relevant official civic authority."
        )

    return answer.strip()