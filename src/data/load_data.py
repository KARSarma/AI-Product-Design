from datasets import load_dataset
import logging

def load_reviews():
    """
    Loads the dataset and verifies its structure.
    """
    logger = logging.getLogger()
    logger.info("Attempting to load dataset...")

    dataset = load_dataset("amazon_polarity")  # Replace with the actual dataset name or path
    logger.info(f"Loaded dataset: {dataset}")

    # Log dataset structure
    if "train" in dataset and "test" in dataset:
        logger.info(f"Train split size: {len(dataset['train'])}")
        logger.info(f"Test split size: {len(dataset['test'])}")
        logger.info(f"Features in dataset: {dataset['train'].features}")
    else:
        logger.error("Dataset does not contain 'train' or 'test' splits.")

    return dataset
