from risk_rules import (
    contains_pattern,
    URGENCY_PATTERNS,
    AUTHORITY_PATTERNS,
    REWARD_PATTERNS,
    FEAR_PATTERNS
)
from url_analyzer import analyze_urls
from explainability import explain


def calculate_risk(message):

    # ✅ Stable return contract
    result = {
        "score": None,
        "risk": "UNKNOWN",
        "reasons": [],
        "signals": {}
    }

    # --- Short / invalid input ---
    if not message or len(message.strip()) < 15:
        result["reasons"].append("Insufficient content to explain risk")
        return result

    # --- Normal processing ---
    text = message.lower()
    score = 0

    if contains_pattern(text, URGENCY_PATTERNS):
        score += 30
        result["reasons"].append("Uses urgency language (+30)")

    if contains_pattern(text, AUTHORITY_PATTERNS):
        score += 25
        result["reasons"].append("Impersonates authority (+25)")

    if contains_pattern(text, REWARD_PATTERNS):
        score += 20
        result["reasons"].append("Promises rewards (+20)")

    if contains_pattern(text, FEAR_PATTERNS):
        score += 30
        result["reasons"].append("Triggers fear or threat (+30)")

    url_score, url_reasons = analyze_urls(message)
    score += url_score
    result["reasons"].extend(url_reasons)

    # --- Explainability layer ---
    explain_reasons, signals = explain(text)
    result["signals"] = signals

    if explain_reasons:
        result["reasons"].extend(explain_reasons)

    # --- Clamp score ---
    score = max(0, min(score, 100))
    result["score"] = score

    # --- Final risk label ---
    if score > 70:
        result["risk"] = "BLOCKED"
    elif score > 40:
        result["risk"] = "SUSPICIOUS"
    else:
        result["risk"] = "SAFE"

    if not result["reasons"]:
        result["reasons"].append("No strong risk signals detected")

    return result