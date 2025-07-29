import streamlit as st
import pickle

model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

st.title("📰 Fake News Detection")

news_text = st.text_area("Enter News Article Text")

if st.button("Check"):
    cleaned = news_text.lower()
    transformed = vectorizer.transform([cleaned])
    prediction = model.predict(transformed)

    if prediction[0] == 0:
        st.error("This looks like **FAKE NEWS** ❌")
    else:
        st.success("This looks like **REAL NEWS** ✅")
