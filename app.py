import streamlit as st
from textblob import TextBlob
import plotly.express as px

st.title("Sentiment Analysis App")

def get_sentiment_str(value):
    if value > 0:
        return "Positive 😁"
    elif value < 0:
        return "Negative 😡"
    else:
        return "Neutral 😶"

def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def get_sentence(text):
    blob = TextBlob(text)
    return blob.sentences

with st.form("f1"):
    text = st.text_area("Enter Your Text Content", height=200)
    is_sentence_wise = st.checkbox("Sentence Wise")
    btn = st.form_submit_button("Analyse")
if btn and text:
    if not is_sentence_wise:
        sentiment = get_sentiment(text)
        sentiment_str = get_sentiment_str(sentiment)
        st.info(sentiment_str)
    else:
        results = {}
        sentences = get_sentence(text)
        for sentence in sentences:
            if "Positive 😁" == get_sentiment_str(sentence.sentiment.polarity):
                if 'Positive 😁' in results:
                    results['Positive 😁'] += 1
                else:
                    results['Positive 😁'] = 1
            elif "Negative 😡" == get_sentiment_str(sentence.sentiment.polarity):
                if 'Negative 😡' in results:
                    results['Negative 😡'] += 1
                else:
                    results['Negative 😡'] = 1
            else:
                if 'Neutral 😶' in results:
                    results['Neutral 😶'] += 1
                else:
                    results['Neutral 😶'] = 1
        st.info(results)
        fig = px.pie(names=results.keys(), values=results.values())
        st.plotly_chart(fig)

# streamlit run .\app.py