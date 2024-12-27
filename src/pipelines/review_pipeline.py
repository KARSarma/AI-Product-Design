import logging
import time
import matplotlib.pyplot as plt
from src.data.load_data import load_reviews
from src.models.nlp_analysis import analyze_sentiment
from src.models.aspect_analysis import analyze_aspects

def summarize_sentiments(reviews, logger):
    """
    Aggregates sentiment analysis results and calculates the percentage of positive and negative reviews.
    """
    positive_count = 0
    negative_count = 0

    logger.info("Summarizing sentiments...")
    for review in reviews[:10]:  # Adjust range for testing or production
        if isinstance(review, dict) and "content" in review:
            text = review["content"]
            sentiment = analyze_sentiment(text)
            logger.info(f"Review: {text[:100]}...\nSentiment: {sentiment}")
            if sentiment["label"] == "POSITIVE":
                positive_count += 1
            elif sentiment["label"] == "NEGATIVE":
                negative_count += 1

    total = positive_count + negative_count
    if total > 0:
        positive_percent = (positive_count / total) * 100
        negative_percent = (negative_count / total) * 100
        logger.info(f"Positive Reviews: {positive_percent:.2f}%")
        logger.info(f"Negative Reviews: {negative_percent:.2f}%")
    else:
        logger.warning("No valid reviews found for summarization.")

def analyze_trends(reviews, logger):
    """
    Analyzes trends in sentiment across reviews and visualizes the results.
    """
    positive_count = 0
    negative_count = 0
    neutral_count = 0

    logger.info("Analyzing sentiment trends...")
    for review in reviews[:100]:  # Limit to first 100 reviews
        if isinstance(review, dict) and "content" in review:
            text = review["content"]
            sentiment = analyze_sentiment(text)
            label = sentiment["label"]

            if label == "POSITIVE":
                positive_count += 1
            elif label == "NEGATIVE":
                negative_count += 1
            else:
                neutral_count += 1

    total = positive_count + negative_count + neutral_count
    if total > 0:
        positive_percent = (positive_count / total) * 100
        negative_percent = (negative_count / total) * 100
        neutral_percent = (neutral_count / total) * 100

        logger.info(f"Positive: {positive_percent:.2f}% | Negative: {negative_percent:.2f}% | Neutral: {neutral_percent:.2f}%")

        labels = ['Positive', 'Negative', 'Neutral']
        sizes = [positive_percent, negative_percent, neutral_percent]
        colors = ['green', 'red', 'gray']
        plt.figure(figsize=(8, 6))
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title("Sentiment Distribution")
        plt.show()
    else:
        logger.warning("No valid reviews found for trend analysis.")

def process_reviews(logger):
    """
    Processes reviews for sentiment analysis, ABSA, and trend analysis.
    """
    logger.info("Attempting to load dataset...")
    reviews = load_reviews()

    # Ensure the "train" split is used
    if "train" not in reviews or len(reviews["train"]) == 0:
        logger.error("No training data found in dataset.")
        return

    train_reviews = reviews["train"][:100]  # Access the first 100 reviews for testing
    logger.info(f"Train split size: {len(train_reviews)}")

    # Sentiment Analysis
    logger.info("Starting sentiment analysis...")
    sentiment_start_time = time.time()
    for review in train_reviews:
        if isinstance(review, dict) and "content" in review:
            text = review["content"]
            sentiment = analyze_sentiment(text)
            logger.info(f"Review: {text[:100]}...\nSentiment: {sentiment}")
        else:
            logger.warning(f"Review is not in expected format: {review}")
    logger.info(f"Sentiment analysis completed in {time.time() - sentiment_start_time:.2f} seconds.")

    # Summarize Sentiments
    summarize_sentiments(train_reviews, logger)

    # Aspect-Based Sentiment Analysis
    analyze_aspects(train_reviews, logger)

    # Trend Analysis
    analyze_trends(train_reviews, logger)

if __name__ == "__main__":
    from src.utils.logger import setup_logger
    logger = setup_logger("logs/pipeline.log")
    logger.info("Pipeline started.")

    process_reviews(logger)

    logger.info("Pipeline completed.")
