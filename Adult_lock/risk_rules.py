import re

# Pattern lists
URGENCY_PATTERNS = [
    "urgent", "act immediately", "act now", "immediately", "asap", "limited time"
]

AUTHORITY_PATTERNS = [
    "admin", "bank", "support", "security", "official", "manager"
]

REWARD_PATTERNS = [
    "win", "bonus", "reward", "prize", "gift", "congratulations"
]

FEAR_PATTERNS = [
    "risk", "danger", "threat", "locked", "suspended", "terminated"
]

def contains_pattern(text, patterns):
    """
    Returns True if any pattern matches the text.
    Case-insensitive substring match.
    """
    text = text.lower()
    for p in patterns:
        if p.lower() in text:
            return True
    return False