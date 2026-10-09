
from src.gemini_client import generate_guidance
from src.knowledge_base import find_relevant_guidance
from src.safety import check_request


def get_response(question: str) -> str:
    """Return safe, informational guidance for a civic question."""

    allowed, message = check_request(question)

    if not allowed:
        return message

    try:
        context = find_relevant_guidance(question)

        answer = generate_guidance(
            question=question,
            guidance_context=context,
        )

        return answer

    except ValueError:
        return (
            "The AI service is not configured yet. Please consult "
            "the relevant official civic authority for guidance."
        )

    except Exception:
        return (
            "Sorry, I couldn't generate guidance right now. Please "
            "consult the relevant official civic authority."
        )
