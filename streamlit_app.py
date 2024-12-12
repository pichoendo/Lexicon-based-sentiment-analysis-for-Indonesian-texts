import streamlit as st
from SentimentAnalysis import SentimentAnalysis

# Inisialisasi kelas
sentiment_analyzer = SentimentAnalysis()
st.title("Lexicon based Sentiment Analyze for Indonesian text")
st.write(
    "Let's start by input some indonesian text on the field"
)
input_text = st.text_input(
    label=f"Indonesian Sentence",
    value=None,
    placeholder="Input indonensian sentence here",
)
if (input_text):
    result = sentiment_analyzer.analysis(input_text)
    st.markdown(
        f'#### Result of {input_text} is {result}'
    )