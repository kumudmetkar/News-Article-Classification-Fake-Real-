# News-Article-Classification-Fake-Real-
# 📰 Fake News Detection Using NLP

A machine learning project that detects whether a news article is **Real** or **Fake** using Natural Language Processing (NLP). This project is built using Python and provides a **Streamlit web app** where users can input news content and get instant predictions.

## 📌 Features

- Classifies news articles as **real** or **fake**
- NLP-based preprocessing (stopwords removal, stemming, etc.)
- TF-IDF vectorization of text
- Logistic Regression classification model
- Web interface using **Streamlit**
- Clean and simple user experience
- 
## 📁 Project Structure
fake-news-detection/
│
├── app.py # Streamlit app code
├── FakeNewsDetector.pkl # Trained ML model
├── tfidf_vectorizer.pkl # TF-IDF Vectorizer
├── notebook.ipynb # Jupyter notebook with training code
├── README.md # Project documentation

## 🧰 Tools & Technologies

- **Python**
- **NLTK** (Natural Language Toolkit)
- **scikit-learn**
- **Pandas**
- **Streamlit**
- **Pickle**


## 🔍 How It Works

1. **Data Collection**: Combined real and fake news datasets from Kaggle.
2. **Preprocessing**: Cleaned and tokenized text using NLTK.
3. **Vectorization**: Converted text into numerical form using TF-IDF.
4. **Model Training**: Logistic Regression used to classify articles.
5. **Web App**: Streamlit used to deploy a user-friendly prediction interface.

Dataset Source
Kaggle: Fake and Real News Dataset

https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

