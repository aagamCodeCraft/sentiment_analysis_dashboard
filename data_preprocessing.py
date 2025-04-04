import pandas as pd
import re
import string

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
    df = preprocess_data(r"C:\Users\aagam\OneDrive\Desktop\Resume project\sentiment_analysis_dashboard\data\Reviews.csv")
    df.to_csv(r"C:\Users\aagam\OneDrive\Desktop\Resume project\sentiment_analysis_dashboard\data\clean_amazon_reviews.csv", index=False)