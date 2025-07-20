import pandas as pd
import re
import string
import os

def clean_text(text):
    if pd.isna(text):
        return ""
    text = text.lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#\w+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    text = re.sub(r'\s{2,}', ' ', text)
    return text.strip()

def preprocess_data(filepath):
    df = pd.read_csv(filepath)
    df['clean_text'] = df['Text'].apply(clean_text)
    return df

if __name__ == "__main__":
    # Ensure the data directory exists
    if not os.path.exists('data'):
        os.makedirs('data')
        
    df = preprocess_data("data/Reviews.csv")
    df.to_csv("data/clean_amazon_reviews.csv", index=False)
    print("Data preprocessing complete. Saved to data/clean_amazon_reviews.csv")