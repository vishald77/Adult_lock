import streamlit as st
# from risk_engine import calculate_risk
# from explanation import risk_meter, recommendation
# from explanation import risk_meter, recommendation, risk_meter

from risk_engine import calculate_risk
from explanation import risk_meter, recommendation

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

        result = calculate_risk(message)

        st.markdown(f"### {result['risk']}")

        if result["score"] is not None:
            score = result["score"]

            if isinstance(score, (int, float)) and score >= 0:
                normalized = min(max(score / 100, 0.0), 1.0)
                st.progress(normalized)

        st.subheader("Why?")
        for r in result["reasons"]:
            st.write("•", r)

        # Accept tuple-like returns of length >=2, ignore extras if present
        if isinstance(result, (list, tuple)):
            if len(result) >= 2:
                score, reasons, *extra = result
            else:
                # st.error("Message too short to analyze")
                st.stop()
        else:
            # st.error("Message too short to analyze")
            st.stop()

        # basic validation / normalization
        try:
            score = float(score)
        except Exception:
            st.error("Risk score returned by calculate_risk is not numeric.")
            st.stop()

        if not isinstance(reasons, (list, tuple)):
            reasons = [str(reasons)]

        st.markdown("## 🔍 Risk Assessment")
        st.markdown(f"### {risk_meter(score)}")
        st.write(f"**Risk Score:** {score}/100")

        with st.expander("Why was this flagged?"):
            if reasons:
                for r in reasons:
                    st.write(f"- {r}")
            else:
                st.write("No suspicious patterns detected.")


        # st.markdown("### Recommendation")
        st.markdown("### ✅ Recommended Action")
        st.info(recommendation(risk_meter(score)))