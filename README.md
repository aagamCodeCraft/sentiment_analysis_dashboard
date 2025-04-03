# sentiment_analysis_dashboard

## Overview
This project analyzes customer reviews or social media mentions and visualizes sentiment trends over time using a dashboard.

## Project Structure
```
sentiment_analysis_dashboard/
├── data/
│   └── amazon_reviews.csv
├── notebooks/
├── src/
│   ├── data_preprocessing.py
│   ├── sentiment_analysis.py
│   └── dashboard.py
├── requirements.txt
└── README.md
```

## Steps
1. **Data Collection:** Use existing dataset (e.g., Amazon Fine Food Reviews).
2. **Data Preprocessing:** Clean the text data.
3. **Sentiment Analysis:** Analyze sentiment using TextBlob.
4. **Dashboard Creation:** Create an interactive dashboard using Streamlit.

## How to Run
1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
2. Preprocess data:
    ```sh
    python src/data_preprocessing.py
    ```
3. Analyze sentiment:
    ```sh
    python src/sentiment_analysis.py
    ```
4. Run the dashboard:
    ```sh
    streamlit run src/dashboard.py
    ```

## Additional Resources for Data
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets.php)
- [Google Dataset Search](https://datasetsearch.research.google.com/)