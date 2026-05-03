import streamlit as st
import pickle

# ✅ LOAD MODEL FIRST (this is what you're missing)
model = pickle.load(open("final_model.pkl", "rb"))
vectorizer = pickle.load(open("word_vectorizer.pkl", "rb"))

st.title("✍️ Authorship Attribution")

text = st.text_area("Enter text")

if st.button("Predict"):
    if text:
        vec = vectorizer.transform([text])
        pred = model.predict(vec)[0]
        st.success(f"Predicted Author: {pred}")
    else:
        st.warning("Enter some text")