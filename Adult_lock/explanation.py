def risk_level(score):
    if score <= 30:
        return "🟢 Safe"
    elif score <= 60:
        return "🟡 Caution"
    else:
        return "🔴 High Risk"


def recommendation(level):
    if "Safe" in level:
        return "No immediate red flags. Stay alert."
    elif "Caution" in level:
        return "Pause and verify the source before acting."
    else:
        return "Do NOT click links. Verify through official channels."
