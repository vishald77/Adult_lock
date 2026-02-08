from risk_rules import (
    contains_pattern,
    URGENCY_PATTERNS,
    AUTHORITY_PATTERNS,
    REWARD_PATTERNS,
    FEAR_PATTERNS
)
from url_analyzer import analyze_urls

def calculate_risk(message):
    

    if not message or len(message.strip()) < 15:
        return {
            "score" : 0,
            "risk": "UNKNOWN",
            "reason": "Content too short to analyze"
        }
   
    else:
        score = 0
        reasons = []

        text = message.lower()

        if contains_pattern(text, URGENCY_PATTERNS):
            score += 30
            reasons.append("Uses urgency language (+30)")

        if contains_pattern(text, AUTHORITY_PATTERNS):
            score += 25
            reasons.append("Impersonates authority (+25)")

        if contains_pattern(text, REWARD_PATTERNS):
            score += 20
            reasons.append("Promises rewards (+20)")

        if contains_pattern(text, FEAR_PATTERNS):
            score += 30
            reasons.append("Triggers fear or threat (+30)")

        url_score, url_reasons = analyze_urls(message)
        score += url_score
        reasons.extend(url_reasons)

    return score, reasons
