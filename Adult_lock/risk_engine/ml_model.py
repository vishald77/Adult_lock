import joblib
import os

MODEL_PATH = "phishing_model.pkl"


try:
    model = joblib.load("phishing_model.pkl")
except:
    model = None

def predict_risk(text: str):
    if model is None:
        return 0

    prob = model.predict_proba([text])[0][1]
    return int(prob * 100)