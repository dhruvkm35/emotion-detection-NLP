# Emotion Detection using Machine Learning

This project implements an **Emotion Detection System** that classifies human emotions from text input using **Natural Language Processing (NLP)** and **Machine Learning** techniques. The model predicts emotions such as *happy, sad, anger, fear, surprise, neutral*, etc., providing insights into sentiment and mood.

---

## 🚀 Features

* Preprocessing text data using NLP techniques (tokenization, stopword removal, stemming/lemmatization).
* Feature extraction with **Bag of Words (BoW)** and **TF-IDF**.
* Emotion classification using **Random Forest Classifier** (or chosen ML model).
* Deployed on **Streamlit** for an interactive web interface.
* Real-time text input with predicted emotion output.

---

## 📊 Tech Stack

* **Python 3**
* **Scikit-learn** – Machine Learning models
* **NLTK / Text preprocessing**
* **Pickle** – Model serialization
* **Streamlit** – Web app deployment

---
2. Create & activate virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

## ▶️ Usage

1. Run the Streamlit app:

```bash
streamlit run app.py
```
2. Enter a sentence in the text box.
3. Click **Predict** to see the detected emotion.
---

## 📂 Project Structure
```
emotion-detection/
│── app.py                 # Streamlit web app  
│── emotion detection.ipynb # Model training notebook  
│── RFmodel.pkl            # Saved ML model  
│── bow.pkl          
│── README.md              # Project documentation  
```
## 📸 Screenshots

(Add screenshots of your Streamlit UI here)

---
## 🔮 Future Improvements

* Add deep learning models (LSTM, BERT).
* Extend to multi-lingual emotion detection.
* Deploy with Docker / Cloud.
