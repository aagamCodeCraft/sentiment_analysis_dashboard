import pandas as pd
from textblob import TextBlob

def analyze_sentiment(text):
    if isinstance(text, str):
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
    else:
        return 'neutral'

def apply_sentiment_analysis(filepath):
    df = pd.read_csv(filepath)
    df['sentiment'] = df['clean_text'].apply(analyze_sentiment)
    return df

if __name__ == "__main__":
    df = apply_sentiment_analysis("data/clean_amazon_reviews.csv")
    df.to_csv("data/sentiment_amazon_reviews.csv", index=False)
    print("Sentiment analysis complete. Saved to data/sentiment_amazon_reviews.csv")