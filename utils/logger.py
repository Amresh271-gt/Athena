# logger.py
import logging
import os

LOG_FILE = "athena.log"

# Create logger
logger = logging.getLogger("AthenaLogger")
logger.setLevel(logging.INFO)

# Check if handler already exists (avoid duplicates)
if not logger.handlers:
    # File handler
    fh = logging.FileHandler(LOG_FILE)
    fh.setLevel(logging.INFO)
    
    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    
    # Add handler
    logger.addHandler(fh)

# Convenience functions
def log_info(message):
    logger.info(message)

def log_error(message):
    logger.error(message)
