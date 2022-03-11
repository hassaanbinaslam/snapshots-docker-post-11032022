##
# app/src/commons/logger.py

import logging
import os

logformat = "%(levelname)s %(asctime)s - %(message)s"
filename = "logfile.log"

# Setting the config of the log object
logging.basicConfig(
    format=logformat,
    filename=filename,
    level=logging.INFO,
)
