import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

data = pd.read_csv("data/phishing_sample.csv")

X = data["text"]
y = data["label"]

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

pipeline.fit(X, y)

joblib.dump(pipeline, "phishing_model.pkl")

print("Model trained & saved")