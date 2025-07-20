import pandas as pd
import streamlit as st
import plotly.express as px

# Load the data using a relative path
try:
    df = pd.read_csv("data/sentiment_amazon_reviews.csv")

    # Title
    st.title("Sentiment Analysis Dashboard")

    # Sentiment Distribution
    st.header("Sentiment Distribution")
    fig = px.histogram(df, x='sentiment', title="Sentiment Distribution", color='sentiment')
    st.plotly_chart(fig)

    # Sentiment Over Time
    st.header("Sentiment Over Time")
    df['Time'] = pd.to_datetime(df['Time'], unit='s')
    df['date'] = df['Time'].dt.date
    sentiment_over_time = df.groupby(['date', 'sentiment']).size().reset_index(name='counts')
    fig = px.line(sentiment_over_time, x='date', y='counts', color='sentiment', title="Sentiment Over Time")
    st.plotly_chart(fig)

except FileNotFoundError:
    st.error("The data file was not found. Please run `data_preprocessing.py` and `sentiment_analysis.py` first.")
