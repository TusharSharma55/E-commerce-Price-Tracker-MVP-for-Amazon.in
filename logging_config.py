import logging
import os

os.makedirs("AllLogs", exist_ok=True)
with open("AllLogs/log_details.log", "a") as file:
    pass

file_handler = logging.FileHandler("AllLogs/log_details.log")
log_formatter = "%(asctime)s ** %(message)s ** %(levelname)s ** %(lineno)s"

formater = logging.Formatter(log_formatter)
