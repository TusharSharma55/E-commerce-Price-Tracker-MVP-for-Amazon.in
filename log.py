import logging

from logging_config import formater, file_handler


def get_logger(name: str = "E_Commerce_Price_Tracker"):
    logger = logging.getLogger(name)
    file_handler.setFormatter(formater)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    return logger
