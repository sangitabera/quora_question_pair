import joblib
from app.utils.text_preprocessing import query_point_creator

model = joblib.load("models/xgboost_classifier.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def predict_duplicate(q1: str, q2: str):

    features = query_point_creator(q1,q2)
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0].max()

    return prediction, probability