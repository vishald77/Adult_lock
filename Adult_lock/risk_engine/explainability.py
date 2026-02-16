def build_explanations(triggers, rule_score, model_score, final_score):
    explanations = []

    # --- Explain rule triggers ---
    for trigger in triggers:
        if "URL" in trigger:
            explanations.append("Contains a suspicious link")

        elif "Multiple phishing keywords" in trigger:
            explanations.append(trigger)

        else:
            explanations.append(f"Suspicious keyword detected: {trigger}")

    # --- Explain multiple signals ---
    if len(triggers) >= 3:
        explanations.append("Multiple scam signals detected")

    # --- Explain ML contribution ---
    if model_score > 70:
        explanations.append("AI model detected phishing pattern")

    # --- Explain scoring confidence ---
    if final_score >= 75:
        explanations.append("High confidence scam detected")
    elif final_score >= 45:
        explanations.append("Message shows suspicious characteristics")

    # --- Fallback if nothing detected ---
    if not explanations:
        explanations.append("No strong scam signals detected")

    # --- Final classification ---
    if final_score >= 75:
        status = "BLOCKED"
    elif final_score >= 45:
        status = "SUSPICIOUS"
    else:
        status = "SAFE"

    explanations.append(f"Message classified as {status}")

    return explanations