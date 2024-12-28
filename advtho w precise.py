import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import nltk # toinstall
from textblob import TextBlob

nltk.download("punkt")
nltk.download("stopwords")

data = pd.read_csv("qualitative.csv")

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

sentiment_results = data['adviceThoughts'].dropna().apply(analyze_sentiment)

data.loc[data['adviceThoughts'].notnull(), 'sentiment_polarity'] = [result[0] for result in sentiment_results]
data.loc[data['adviceThoughts'].notnull(), 'sentiment_subjectivity'] = [result[1] for result in sentiment_results]

data_sentiment_with_bonus = data[['adviceThoughts', 'sentiment_polarity', 'sentiment_subjectivity', 'total_bonus', 'con.precise']]

print(data_sentiment_with_bonus.head())

# Save the sentiment analysis results with bonus to a CSV file
chu = 'sentiment_analysis_w_bonus_precise.csv'
data_sentiment_with_bonus.to_csv(chu, index=False)
