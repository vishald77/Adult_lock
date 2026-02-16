from risk_engine.rules import rule_score
from risk_engine.ml_model import predict_risk
from risk_engine.explainability import build_explanations

def analyze_message(text: str):
    rule_score_value, triggers = rule_score(text)
    model_score = predict_risk(text)

    # final_score = int((rule_score_value * 0.6) + (model_score * 0.4))
    final_score = int((rule_score_value * 0.7) + (model_score * 0.3))
    
    result = {
        "score": final_score,
        "risk": None,
        "explanations": []
    }
    
    if final_score >= 75:
        result["risk"] = "BLOCKED"
    elif final_score >= 40:
        result["risk"] = "SUSPICIOUS"
    else:
        result["risk"] = "SAFE"

    result["explanations"] = build_explanations(
        triggers,
        rule_score_value,
        model_score,
        final_score
    )
    print("RULE SCORE:", rule_score_value)
    print("MODEL SCORE:", model_score)
    print("FINAL SCORE:", final_score)
    return result