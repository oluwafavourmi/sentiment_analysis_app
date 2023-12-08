import nltk
import streamlit as st
import joblib

model = open('sentiment analysis.pkl', 'rb')
sent_anal_model = joblib.load(model)

def output(input):
    input_as_string = str(input)
    prediction = sent_anal_model.polarity_scores(input)

    if prediction['neg']>=0.5 and prediction['neu']<=0.49 and prediction['pos']<=0.49:
        print('bad')
    elif prediction['neg']<=0.49 and prediction['neu']>=0.50 and prediction['pos']<=0.49:
        print('neither good nor bad')
    elif prediction['neg']<=0.5 and prediction['neu']<=0.49 and prediction['pos']>=0.49:
        print('Good')
        return prediction


def run():
    st.title('Sentiment Analysis Web App')
    Label ='This is for sentiment analysis'
    input = st.text_input(label=Label, value="", 
                  max_chars=100, key=str, type="default", help=None, 
                  autocomplete=None, on_change=None, args=None, kwargs=None, 
                  placeholder="Enter your review sentence here", 
                  disabled=False, label_visibility="visible")
    final_display = ""
    if st.button('Check Comment'):
        final_display = output(input)
        st.success('This comment is {}'.final_display)

if __name__ =='__main__':
    run()
        