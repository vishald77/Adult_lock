

def build_explanations(rule_triggers, rule_score, model_score, final_score):
    """
    Builds human-readable explanations.
    """

    explanations = []

    # include rule triggers
    if rule_triggers:
        explanations.extend(rule_triggers)

    # model insight
    if model_score >= 70:
        explanations.append("ML model strongly indicates phishing pattern")
    elif model_score >= 40:
        explanations.append("ML model detected suspicious patterns")

    # final risk reasoning
    if final_score >= 75:
        explanations.append("Message classified as HIGH RISK")
    elif final_score >= 45:
        explanations.append("Message classified as SUSPICIOUS")
    else:
        explanations.append("Message appears safe")

    return explanations