
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
GUIDANCE_FILE = PROJECT_ROOT / "data" / "grievance_guidance.json"


def load_guidance() -> dict:
    """Load civic grievance guidance from the JSON file."""
    if not GUIDANCE_FILE.exists():
        raise FileNotFoundError(
            f"Guidance file not found: {GUIDANCE_FILE}"
        )

    with GUIDANCE_FILE.open("r", encoding="utf-8") as file:
        guidance = json.load(file)

    if not isinstance(guidance, dict):
        raise ValueError("Guidance data must be a JSON object.")

    if not isinstance(guidance.get("categories"), list):
        raise ValueError(
            "Guidance data must contain a categories list."
        )

    return guidance


def find_relevant_guidance(question: str) -> str:
    """Find civic guidance related to a citizen's question."""
    if not question or not question.strip():
        return "Please enter a question."

    guidance = load_guidance()
    question_words = set(question.lower().split())
    relevant_sections = []

    for category in guidance["categories"]:
        name = category.get("name", "")
        description = category.get("description", "")
        process = category.get("general_process", [])

        searchable_text = (
            name + " " + description + " " + " ".join(process)
        ).lower()

        if any(word in searchable_text for word in question_words):
            relevant_sections.append(
                f"Category: {name}\n"
                f"Description: {description}\n"
                f"General process: {' '.join(process)}"
            )

    if not relevant_sections:
        return (
            "No directly matching category was found in the guidance "
            "data. Ask the citizen to consult the relevant official "
            "municipal or utility website."
        )

    return "\n\n".join(relevant_sections)
