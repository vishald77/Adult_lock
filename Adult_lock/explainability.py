def explain(text: str):
    """
    Returns:
      - explanations: list of explanations detected in text
      - signals: dictionary of words/urls detected
    """
    explanations = []
    signals = {}

    urgent_words = ["urgent", "immediately", "act now", "limited time", "asap"]
    money_words = ["bank", "account", "payment", "otp", "credit", "security"]
    reward_words = ["win", "bonus", "reward", "prize", "gift", "congratulations"]

    found_urgent = [w for w in urgent_words if w in text.lower()]
    found_money = [w for w in money_words if w in text.lower()]
    found_reward = [w for w in reward_words if w in text.lower()]

    if found_urgent:
        explanations.append("Urgent language detected")
        signals["urgent_words"] = found_urgent

    if found_money:
        explanations.append("Financial or account-related terms found")
        signals["money_keywords"] = found_money

    if found_reward:
        explanations.append("Promises reward detected")
        signals["reward_keywords"] = found_reward

    if "http" in text.lower():
        explanations.append("Contains a link")
        signals["url_present"] = True
    assert isinstance(explanations, list)
    return explanations, signals