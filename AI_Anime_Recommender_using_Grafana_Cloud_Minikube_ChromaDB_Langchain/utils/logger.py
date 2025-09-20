import logging
import os
from datetime import datetime

# Create a directory named - logs
LOGS_DIR='logs'
os.mkdirs(LOGS_DIR,exists_ok=True)

# Save the logs in the directory
LOG_FILE= os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

# Creating the logging configuration.
logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s- %(levelname)s -%(message)s',
    level= logging.DEBUG
)

def get_logger(name):
    logger= logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger