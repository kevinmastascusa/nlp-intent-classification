import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    # Perform sentiment analysis using NLTK's SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    
    # Determine the sentiment label based on the scores
    if sentiment_scores["compound"] >= 0.05:
        sentiment_label = "Positive"
    elif sentiment_scores["compound"] <= -0.05:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"
    
    return sentiment_label

# User interface loop
while True:
    user_input = input("Enter pathology report text (or 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    sentiment = analyze_sentiment(user_input)
    print("Sentiment:", sentiment)
    print()
