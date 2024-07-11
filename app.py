import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

# Load the vectorizer and model
with open('vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

with open('naive_bayes_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Preprocess the input text
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_tweet(tweet):
    tweet = re.sub(r"http\S+", "", tweet)  # Remove URLs
    tweet = re.sub(r"@\S+", "", tweet)     # Remove mentions
    tweet = re.sub(r"#\S+", "", tweet)     # Remove hashtags
    tweet = re.sub(r"[^A-Za-z\s]", "", tweet)  # Remove special characters and numbers
    tweet = tweet.lower()                  # Convert to lowercase
    words = tweet.split()                  # Tokenization
    words = [stemmer.stem(word) for word in words if word not in stop_words]  # Remove stop words and stemming
    return " ".join(words)

# Streamlit app
st.title("Twitter Sentiment Analysis Project")
st.write("Enter a tweet for sentiment analysis:")

user_input = st.text_area("Tweet")

if st.button("Analyze"):
    if user_input:
        processed_input = preprocess_tweet(user_input)
        input_vectorized = vectorizer.transform([processed_input])
        prediction = model.predict(input_vectorized)
        
        st.write(f"Sentiment: **{prediction[0]}**")
    else:
        st.write("Please enter a tweet to analyze.")

