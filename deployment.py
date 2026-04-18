# streamlit_app.py

import streamlit as st
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer

# Helper: safe load
def safe_load(path):
    try:
        return joblib.load(path)
    except Exception as e:
        return None

# Try loading model and vectorizer from project root first
model = safe_load('linearSVC_model.joblib')
vectorizer = safe_load('tfidf_vectorizer.joblib')

# Also try loading EDA artifacts (if present) for showing EDA summaries
EDA_DIR = 'eda_artifacts'
eda = {}
if os.path.isdir(EDA_DIR):
    for fname in os.listdir(EDA_DIR):
        if fname.endswith('.joblib'):
            key = fname.replace('eda_', '').replace('.joblib', '')
            eda[key] = safe_load(os.path.join(EDA_DIR, fname))

st.title("Sentiment Analysis Deployment")

st.subheader("Predict sentiment")
user_input = st.text_area("Enter your review text:", "")

def predict_sentiment(text):
    if vectorizer is None or model is None:
        st.error('Model or vectorizer not found. Make sure `linearSVC_model.joblib` and `tfidf_vectorizer.joblib` exist.')
        return None
    X_vect = vectorizer.transform([text])
    pred = model.predict(X_vect)[0]
    return pred

if st.button("Analyze"):
    if not user_input.strip():
        st.write("Enter text to analyze.")
    else:
        prediction = predict_sentiment(user_input)
        if prediction is not None:
            st.write(f"Predicted Sentiment: **{prediction}**")
