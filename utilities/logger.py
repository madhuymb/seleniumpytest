import logging
import os
from datetime import datetime

class Logger:
    @staticmethod
    def get_logger(name="automation"):
        """Create and return a logger instance."""

        # Create logs directory if it doesn't exist
        logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports", "logs")
        os.makedirs(logs_dir, exist_ok=True)

        # Create log file with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_file = os.path.join(logs_dir, f"test_log_{timestamp}.log")

        # Create a custom logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        # Prevent duplicate handlers if called multiple times
        if not logger.handlers:
            # File handler
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)

            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)

            # Log format
            formatter = logging.Formatter(
                fmt="%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # Add handlers
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger
