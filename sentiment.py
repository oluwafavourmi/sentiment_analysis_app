import nltk
import streamlit as st
import joblib
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
    


def output(input):
    analyzer = SentimentIntensityAnalyzer()
    prediction = analyzer.polarity_scores(input)
    text = ""
    if prediction['neg']>=0.5 and prediction['neu']<=0.49 and prediction['pos']<=0.49:
        text='This comment is bad'
    elif prediction['neg']<=0.49 and prediction['neu']>=0.50 and prediction['pos']<=0.49:
        text='This comment is neither good nor bad'
    elif prediction['neg']<=0.49 and prediction['neu']<=0.49 and prediction['pos']>=0.50:
        text = 'This comment is Good'

    return text



st.title('Sentiment Analysis Web App')
input = st.text_input('Enter Your Phrase Here')
final_display = ""
if st.button('Check Comment'):
    final_display = output(input)
    st.success(final_display)


        