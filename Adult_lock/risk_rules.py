import re
import validators
from urllib.parse import urlparse

URGENCY_PATTERNS = [
    "act now", "immediately", "urgent", "within 24 hours",
    "limited time", "asap"
]

AUTHORITY_PATTERNS = [
    "bank", "police", "government", "tax", "hr",
    "manager", "security team"
]

REWARD_PATTERNS = [
    "won", "winner", "prize", "refund", "cashback", "bonus"
]

FEAR_PATTERNS = [
    "account blocked", "suspended", "legal action",
    "verify immediately", "unauthorized activity"
]


def contains_pattern(text, patterns):
    return any(pat in text.lower() for pat in patterns)
