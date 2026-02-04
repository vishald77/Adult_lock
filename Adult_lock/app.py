import streamlit as st
from risk_engine import calculate_risk
from explanation import risk_level, recommendation

st.set_page_config(page_title="Adult Lock v2", layout="centered")

st.title("🛡️ Adult Lock v2")
st.caption("Explainable fraud awareness for adults")

message = st.text_area(
    "Paste the message or link you received:",
    height=150
)

if st.button("Analyze Risk"):
    if not message.strip():
        st.warning("Please enter a message.")
    else:
        score, reasons = calculate_risk(message)
        level = risk_level(score)

        st.subheader(level)
        st.write(f"**Risk Score:** {score}")

        st.markdown("### Why this was flagged")
        if reasons:
            for r in reasons:
                st.write(f"- {r}")
        else:
            st.write("No suspicious patterns detected.")

        st.markdown("### Recommendation")
        st.info(recommendation(level))
