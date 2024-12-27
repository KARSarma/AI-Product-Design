from transformers import pipeline, AutoTokenizer
import logging

# Initialize the model and tokenizer explicitly
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
sentiment_analyzer = pipeline("sentiment-analysis", model=model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def analyze_sentiment(text):
    """
    Analyzes sentiment of a given text.
    Handles long text by truncating to the model's maximum token length.
    """
    logger = logging.getLogger()
    try:
        max_length = tokenizer.model_max_length
        tokenized_inputs = tokenizer(text, truncation=True, max_length=max_length, return_tensors="pt")
        truncated_text = tokenizer.decode(tokenized_inputs["input_ids"][0], skip_special_tokens=True)

        logger.info(f"Truncated review text: {truncated_text[:100]}...")  # Log first 100 chars of truncated text
        result = sentiment_analyzer(truncated_text)
        logger.info(f"Sentiment analysis result: {result}")
        return result[0]
    except Exception as e:
        logger.error(f"Error during sentiment analysis: {e}")
        return {"label": "ERROR", "score": 0.0}
