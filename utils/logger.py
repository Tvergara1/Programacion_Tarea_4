import logging

logging.basicConfig(
    filename="logs/app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_error(msg):
    logging.error(msg)

def log_event(msg):
    logging.info(msg)