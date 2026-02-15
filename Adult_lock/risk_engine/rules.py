import re

SUSPICIOUS_KEYWORDS = [
    "urgent", "verify", "password", "bank", "login",
    "account", "click", "confirm", "security"
]

def rule_score(text: str):
    score = 0
    triggers = []
    found_keywords=[]

    text_lower = text.lower()

    for word in SUSPICIOUS_KEYWORDS:
        if word in text_lower:
            score += 10
            # triggers.append(f"Suspicious keyword detected: {word}")
            found_keywords.append(word)
    
    if found_keywords:
        score += len(found_keywords) * 10
        triggers.append(
            "Multiple phishing keywords detected (" +
            ", ".join(found_keywords) + ")"
    )

    urls = re.findall(r'(https?://\S+)', text)
    if urls:
        score += 20
        triggers.append("Contains URL")

    if re.search(r'[!?]{2,}', text):
        score += 10
        triggers.append("Excessive punctuation")

    return score, triggers