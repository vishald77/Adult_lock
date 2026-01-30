import streamlit as st
import re

# SCAM_KEYWORDS = [
#     "urgent", "verify", "account", "suspended",
#     "click", "immediately", "refund", "lottery", "prize"
# ]

URGENCY_WORDS = [
    "urgent", "immediately", "act now", "within 24 hours", "last chance"
]

AUTHORITY_WORDS = [
    "bank", "kyc", "income tax", "irs", "customs",
    "delivery", "dhl", "post", "government"
]

REWARD_WORDS = [
    "won", "prize", "lottery", "refund", "cashback"
]


def analyze_message(text):
    text = text.lower()
    score = 0
    reasons = []

    # for word in SCAM_KEYWORDS:
    #     if word in text:
    #         score += 1
    #         reasons.append(f"Contains risky word: '{word}'")

    # if re.search(r"http[s]?://", text):
    #     score += 1
    #     reasons.append("Contains a link")

    # if re.search(r"\b\d{10,}\b", text):
    #     score += 1
    #     reasons.append("Contains long numeric string")

    # return score, reasons
    for word in URGENCY_WORDS:
        if word in text:
            score += 1
            reasons.append("Creates urgency or panic")

    for word in AUTHORITY_WORDS:
        if word in text:
            score += 1
            reasons.append("Pretends to be a trusted authority")

    for word in REWARD_WORDS:
        if word in text:
            score += 1
            reasons.append("Promises reward or money")

    return score, reasons

st.set_page_config(page_title="Adult Lock", page_icon="🛡️")

st.title("🛡️ Adult Lock")
st.caption("Think before you click.")

user_input = st.text_area(
    "Paste the message or link you received:",
    height=150
)

if st.button("Scan Message"):
    if not user_input.strip():
        st.warning("Please paste a message first.")
    else:
        score, reasons = analyze_message(user_input)

        if score >= 4:
            st.error("🚨 HIGH RISK — Likely scam")
        elif score >= 2:
            st.warning("⚠️ MEDIUM RISK — Be cautious")
        else:
            st.success("✅ LOW RISK — Probably safe")

        st.subheader("Why?") 

        for r in reasons:
            st.write("•", r)

        st.subheader("What should you do?")

        if score >= 4:
            st.write("❌ Do NOT click the link")
            st.write("❌ Do NOT reply to the message")
            st.write("✅ Delete it immediately")
            st.write("✅ Verify through official app or website")

        elif score >= 2:
            st.write("⚠️ Pause before clicking")
            st.write("🔍 Check the sender carefully")
            st.write("📞 Confirm via official source")

        else:
            st.write("✅ Looks safe")
            st.write("⚠️ Never share OTPs, passwords, or bank details")
