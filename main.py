import yaml
from src.utils.logger import setup_logger

def main():
    # Load configuration
    with open("config/config.yaml", "r") as file:
        config = yaml.safe_load(file)

    # Initialize logger
    logger = setup_logger(config["logging"]["log_file"])
    logger.info("AI Product Design Project Initialized")
    logger.info(f"Loaded Configuration: {config}")

if __name__ == "__main__":
    main()
