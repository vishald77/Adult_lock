from risk_rules import contains_pattern, URGENCY_PATTERNS, AUTHORITY_PATTERNS, REWARD_PATTERNS, FEAR_PATTERNS
from explainability import explain

def analyze_urls(message):
    """
    Dummy URL analyzer for testing.
    Returns score + explanations for URLs.
    """
    urls = []
    score = 0
    explanations = []

    for word in message.split():
        if word.startswith("http") or word.startswith("www."):
            urls.append(word)
            score += 20
            explanations.append("Contains suspicious link")

    return score, explanations

def calculate_risk(message):
    result = {
        "score": None,
        "risk": "UNKNOWN",
        "explanations": [],
        "signals": {}
    }

    if not message or len(message.strip()) < 15:
        result["explanations"].append("Insufficient content to explain risk")
        return result

    text = message.lower()
    score = 0

    if contains_pattern(text, URGENCY_PATTERNS):
        score += 30
        result["explanations"].append("Uses urgency language (+30)")

    if contains_pattern(text, AUTHORITY_PATTERNS):
        score += 25
        result["explanations"].append("Impersonates authority (+25)")

    if contains_pattern(text, REWARD_PATTERNS):
        score += 20
        result["explanations"].append("Promises rewards (+20)")

    if contains_pattern(text, FEAR_PATTERNS):
        score += 30
        result["explanations"].append("Triggers fear or threat (+30)")

    url_score, url_explanations = analyze_urls(message)
    score += url_score
    # result["explanations"].extend(url_explanations)
    if isinstance(url_explanations, list):
        result["explanations"].extend(url_explanations)
    elif isinstance(url_explanations, str):
        result["explanations"].append(url_explanations)

    # Explain layer
    explain_explanations, signals = explain(text)
    if not isinstance(signals, dict):
        signals = {}
    result["signals"] = signals

    if explain_explanations:
        if isinstance(explain_explanations, list):
            result["explanations"].extend(explain_explanations)
        # elif isinstance(explain_explanations, str):
        #     result["explanations"].append(explain_explanations)

    # Clamp score
    score = max(0, min(score, 100))
    result["score"] = score

    # Risk label
    if score > 70:
        result["risk"] = "BLOCKED"
    elif score > 40:
        result["risk"] = "SUSPICIOUS"
    else:
        result["risk"] = "SAFE"

    if not result["explanations"]:
        result["explanations"].append("No strong risk signals detected")

    return result