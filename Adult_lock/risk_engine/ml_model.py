import joblib
import os

MODEL_PATH = "phishing_model.pkl"

model = None

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)

def predict_risk(text: str) -> int:
    """
    Returns ML probability score (0-100)
    """
    if model is None:
        return 0

    probability = model.predict_proba([text])[0][1]
    return int(probability * 100)