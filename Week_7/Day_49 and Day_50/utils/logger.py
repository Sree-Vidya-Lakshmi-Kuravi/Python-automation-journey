import os
import logging
from  config import config_reader

def setup_logger():
    # Verify the existence of the log file path and create directories if they don't exist
    log_file_path = config_reader.get_log_file()
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    # Create or get a logger
    logger = logging.getLogger("API_Automation_Logger")
    logger.setLevel(config_reader.get_log_level())

    # Prevent the duplicate logging
    if not logger.handlers:
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] (%(filename)s:%(lineno)s) - %(message)s")

        # Create a file handler
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    
    return logger

# Pre-instantiate logger for easy importing everywhere
logger = setup_logger()