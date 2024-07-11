**Twitter Sentiment Analysis with Streamlit**
* This project is a Twitter Sentiment Analysis application built using Streamlit. It classifies tweets into four sentiment categories: positive, negative, neutral, and irrelevant. The application uses a Multinomial Naive Bayes classifier trained on a dataset of tweets.

**Table of Contents**
* Installation
* Usage
* Features
* Project Structure
* Model Training

**Installation**
* Prerequisites:
* Ensure you have Python 3.7 or higher installed. Install the required Python packages using pip:
  * pip install streamlit scikit-learn nltk
* NLTK Stopwords:
  * Download the NLTK stopwords:
  * import nltk
  * nltk.download('stopwords')
* Clone the Repository
  * Clone this repository to your local machine:
  * git clone https://github.com/your-username/twitter-sentiment-analysis.git
  * cd twitter-sentiment-analysis
* Required Files
  * Ensure you have the following files in the project directory:

    * vectorizer.pkl
    * naive_bayes_model.pkl
* These files are the trained CountVectorizer and Multinomial Naive Bayes model, respectively.
* Run the Streamlit app using the following command:
    * streamlit run app.py

 
**Features**
* Real-time Sentiment Analysis: Enter a tweet and get instant sentiment classification.
* User-Friendly Interface: Simple and intuitive web interface built with Streamlit.
* Preprocessing: Automatic text preprocessing including removing URLs, mentions, hashtags, special characters, and stop words.


**Project Structure**
 * twitter-sentiment-analysis/
  * │
  * ├── app.py                  # Streamlit app script
  * ├── vectorizer.pkl          # Trained CountVectorizer
  * ├── naive_bayes_model.pkl  # Trained Naive Bayes model
  * ├── README.md               # Project README file


**Model Training**
* To train the model and create the pickle files (vectorizer.pkl and naive_bayes_model.pkl), follow these steps:

 * Preprocess the Data: Clean and preprocess the tweet data.
 * Vectorize the Data: Use CountVectorizer to transform the text data into numerical features.
 * Train the Model: Train Gaussian, Multinomial, Bernoulli Naive Bayes classifier on the vectorized data.
 * Model Selection: Check the accuracy of all three models, and figure out which one would give the best results (Multinimial in our case).
 * Save the Model and Vectorizer: Save the trained model and vectorizer using pickle.


