def explain(text: str):
    reasons = []
    signals = {}

    urgent_words = ["urgent", "immediately", "act now", "limited time"]
    money_words = ["bank", "account", "payment", "otp", "credit"]

    found_urgent = [w for w in urgent_words if w in text.lower()]
    found_money = [w for w in money_words if w in text.lower()]

    if found_urgent:
        reasons.append("Urgent language detected")
        signals["urgent_words"] = found_urgent

    if found_money:
        reasons.append("Financial or account-related terms found")
        signals["money_keywords"] = found_money

    if "http" in text.lower():
        reasons.append("Contains a link")
        signals["url_present"] = True

    return reasons, signals