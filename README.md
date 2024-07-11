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
    * multiclass_naive_bayes_model.pkl
* These files are the trained CountVectorizer and Multinomial Naive Bayes model, respectively.
* Run the Streamlit app using the following command:
    * streamlit run app.py



