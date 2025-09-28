import streamlit as st
import pickle

# Load model and vectorizer
model_rfc = pickle.load(open('RFmodel.pkl','rb'))
bow = pickle.load(open('bow.pkl','rb'))

st.header('Emotion Detection Model')

# Input
user_input = st.text_area("Enter your sentence",height=150,max_chars=500)

if st.button('Predict'):
    if user_input.strip() != "":
        # query
        query = [user_input]
        prediction = model_rfc.predict(bow.transform(query))[0]

        if prediction == 0:
            emotion = "Joy"
        elif prediction == 1:
            emotion = "Sadness"
        elif prediction == 2:
            emotion = "Anger"
        elif prediction == 3:
            emotion = "Fear"
        elif prediction == 4:
            emotion = "love"
        elif prediction == 5:
            emotion = "surprise"
        else:
            emotion = "Unknown"

        st.success(f'Predicted Emotion: {emotion}')
    else:
        st.warning('Please enter some text to predict')
