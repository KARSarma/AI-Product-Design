from src.models.nlp_analysis import analyze_sentiment
import logging

def extract_aspects(reviews):
    """
    Extracts and categorizes review text into specific aspects such as comfort, durability, and style.
    """
    aspects = {"comfort": [], "durability": [], "style": []}

    for review in reviews:
        if isinstance(review, dict) and "content" in review:
            text = review["content"].lower()

            # Check for specific aspect keywords and categorize accordingly
            if "comfort" in text:
                aspects["comfort"].append(text)
            if "durability" in text:
                aspects["durability"].append(text)
            if "style" in text:
                aspects["style"].append(text)

    return aspects

def analyze_aspects(reviews, logger):
    """
    Analyzes sentiment for each extracted aspect and logs the results.
    """
    aspects = extract_aspects(reviews)

    for aspect, phrases in aspects.items():
        logger.info(f"\nAspect: {aspect}")
        if not phrases:
            logger.warning(f"No reviews found for aspect: {aspect}")
            continue

        for phrase in phrases:
            sentiment = analyze_sentiment(phrase)
            logger.info(f"Phrase: {phrase}\nSentiment: {sentiment}\n")
