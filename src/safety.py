import re

# Requests that the chatbot must not perform
BLOCKED_PATTERNS = [
    r"\b(register|submit|file|lodge)\s+(a\s+)?complaint\b",
    r"\b(track|check)\s+(my\s+)?complaint\s+status\b",
    r"\bguarantee(d|s)?\s+(a\s+)?resolution\b",
    r"\bpromise\s+(me\s+)?(a\s+)?resolution\b",
]


def check_request(question: str) -> tuple[bool, str]:
    """
    Check whether a question asks the chatbot to perform
    an action that is outside the project's scope.
    """
    if not question or not question.strip():
        return False, "Please enter a question."

    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, question, re.IGNORECASE):
            return (
                False,
                "I can explain civic grievance procedures and official "
                "channels, but I cannot register complaints, track "
                "complaint status, or guarantee resolution."
            )

    return True, ""