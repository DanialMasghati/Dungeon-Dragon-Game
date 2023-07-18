import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_FILE = "dungeon.log"


def configure_logging():
    logging.basicConfig(filename=LOG_FILE,
                        level=logging.INFO, format=LOG_FORMAT)


def log_messages():
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')


# configure_logging()
# log_messages()
