import os
import logging
from tqdm import tqdm


class Logs:
    """A class for setting up and managing loggers for file and console output."""

    def __init__(self) -> None:
        """Initialize the Logs class and create a directory for log files if it doesn't exist."""

        if not os.path.exists("logs"):
            os.mkdir("logs")

    def get_file_logger(self, name) -> logging.Logger:
        """Create and configure a file-based logger."""

        # Initialize the logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        # Configure file handler
        handler = logging.FileHandler("logs/stock.log", mode="w")
        handler.setLevel(logging.INFO)
        handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )

        # Add the file handler to the logger
        logger.addHandler(handler)
        return logger

    def get_console_logger(self, name) -> logging.Logger:
        """Create and configure a console-based logger compatible with tqdm progress bars."""

        # Initialize the logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        # Define a custom logging handler compatible with tqdm
        class TqdmLoggingHandler(logging.Handler):
            def emit(self, record):
                """Emit a log record using tqdm.write to avoid interference with progress bars."""

                msg = self.format(record)
                tqdm.write(msg)

        # Configure the custom tqdm-compatible handler
        handler = TqdmLoggingHandler()
        handler.setLevel(logging.INFO)
        handler.setFormatter(logging.Formatter("%(message)s"))

        # Add the custom handler to the logger
        logger.addHandler(handler)
        return logger
