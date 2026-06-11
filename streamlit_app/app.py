import requests
import streamlit as st

st.title("Quora Duplicate Question Detector")

q1 = st.text_area("Question 1")
q2 = st.text_area("Question 2")

if st.button("Predict"):

    payload = {
        "question1": q1,
        "question2": q2
    }

    response = requests.post(
        "http://localhost:8000/predict",
        json=payload
    )

    result = response.json()

    st.success(
        f"{result['prediction']} "
        f"({result['confidence']:.2%})"
    )