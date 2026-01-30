import re

SCAM_KEYWORDS = [
    "urgent", "verify", "account", "suspended",
    "click", "immediately", "refund", "lottery", "prize"
]

def analyze_message(text):
    text = text.lower()
    score = 0
    reasons = []

    for word in SCAM_KEYWORDS:
        if word in text:
            score += 1
            reasons.append(f"Contains risky word: '{word}'")

    if re.search(r"http[s]?://", text):
        score += 1
        reasons.append("Contains a link")

    if re.search(r"\b\d{10,}\b", text):
        score += 1
        reasons.append("Contains long numeric string")

    return score, reasons


msg = input("\nPaste the message or link:\n> ")

score, reasons = analyze_message(msg)

print("\n🛡️ ADULT LOCK RESULT")

if score >= 4:
    print("🚨 HIGH RISK – Likely scam")
elif score >= 2:
    print("⚠️ MEDIUM RISK – Be cautious")
else:
    print("✅ LOW RISK – Probably safe")

print("\nReasons:")
for r in reasons:
    print(" -", r)
