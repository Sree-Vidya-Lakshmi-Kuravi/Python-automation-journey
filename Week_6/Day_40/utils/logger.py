import os
import logging
from datetime import datetime

class CustomLogger:
    """Singleton Logger class to provide a unified logger instance across the framework."""

    @staticmethod
    def get_logger():
        # Create or get logger instance
        logger = logging.getLogger("AutomationFramework")

        # Setting the minimum severity
        logger.setLevel(logging.INFO)

        # If handlers exist, return existing logger
        if logger.hasHandlers():
            return logger

        # Ensuring logs/ folder exists
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)

        # Create timestamp log filename
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_file_path = os.path.join(log_dir, f"automation_{timestamp}.log")

        # Defining standard log msg format
        log_format = logging.Formatter(
            "%(asctime)s [%(levelname)s] (%(filename)s:%(lineno)d) - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S")

        # File Handler - Writes logs to text file
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)

        # Stream Handler - Prints logs to terminal console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_format)
        logger.addHandler(console_handler)     
        return logger   