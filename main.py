import yaml
from src.utils.logger import setup_logger
from src.pipelines.review_pipeline import process_reviews

def main():
    """
    Main entry point for running the review pipeline.
    """
    try:
        # Load configuration file
        with open("config/config.yaml", "r") as file:
            config = yaml.safe_load(file)

        # Initialize logger
        logger = setup_logger(config["logging"]["log_file"])
        logger.info("AI Product Design Project Initialized")
        logger.info(f"Loaded Configuration: {config}")

        # Run the review processing pipeline
        process_reviews(logger)

    except FileNotFoundError as e:
        print(f"Configuration file not found: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
