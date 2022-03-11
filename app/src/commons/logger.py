##
# app/src/commons/logger.py

import logging
import os


if not os.path.exists("logs"):
    os.makedirs("logs")

logformat = "%(levelname)s %(asctime)s - %(message)s"
filename = "logfile.log"


# Setting the config of the log object
logging.basicConfig(
    format=logformat,
    filename=filename,
    level=logging.INFO,
)
