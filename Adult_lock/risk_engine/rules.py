import re

SUSPICIOUS_KEYWORDS = [
    "urgent","verify","bank","login","account","password",
    "reward","bonus","prize","gift","claim",
    "crypto","wallet","bitcoin","transfer"
]

COURIER_PATTERNS = ["customs", "package on hold", "unpaid fees", "return to sender", "confirm delivery"]

crypto_words = ["crypto","wallet","bitcoin","bonus","reward"]


def rule_score(text: str):
    score = 0
    triggers = []
    found_keywords=[]

    text_lower = text.lower()

    if any(word in text.lower() for word in crypto_words):
        triggers.append("Cryptocurrency reward/bonus request")
        score += 30

    for pattern in COURIER_PATTERNS:
        if pattern.lower() in text.lower():
            triggers.append(f"Courier / customs scam detected: {pattern}")
            score += 25

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