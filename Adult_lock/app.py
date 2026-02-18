import streamlit as st
# from risk_engine import calculate_risk
# from explanation import risk_meter, recommendation
# from explanation import risk_meter, recommendation, risk_meter
from highlighter import highlight_text
from risk_engine.ensemble import analyze_message

from risk_engine.risk_engine import calculate_risk
from explanation import risk_meter, recommendation


DEBUG = True

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
        # score, reasons = calculate_risk(message)
      
        # result = calculate_risk(message)
        result = analyze_message(message)

        # --- Highlight risky content ---
        if isinstance(result.get("signals"), dict) and result["signals"]:
            highlighted = highlight_text(message, result["signals"])
            st.markdown("### Highlighted Risky Content")
            st.markdown(highlighted, unsafe_allow_html=True)
        # --- Risk label ---
        st.markdown(f"### {result['risk']}")

        # --- Progress bar ---
        score = result.get("score", 0)
        if isinstance(score, (int, float)) and score >= 0:
            st.progress(min(max(score / 100, 0.0), 1.0))

        # --- Reasons ---
        st.subheader("Why?")

        # fetch explanations from risk engine
        explanations = result.get("explanations", [])

        # guard: make sure it's a list of strings
        if isinstance(explanations, str):
            explanations = [explanations]

        # flatten nested lists if explain() ever returns a list inside a list
        flat_explanations = []
        for item in explanations:
            if isinstance(item, list):
                flat_explanations.extend(item)
            else:
                flat_explanations.append(str(item))  # convert anything else to string

        # render
        if not flat_explanations:
            st.write("• No strong risk signals detected")
        else:
            for e in flat_explanations:
                st.write("•", e)

        # --- Recommendation ---
        st.markdown("### ✅ Recommended Action")
        st.info(recommendation(result["risk"]))

        if DEBUG and "debug" in result:
            st.divider()
            st.write("🔍 Debug Info")
            st.write("Rule Score:", result["debug"]["rule_score"])
            st.write("Model Score:", result["debug"]["model_score"])
            st.write("Final Score:", result["score"])