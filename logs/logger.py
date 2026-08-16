import logging
import os
from datetime import datetime

logging.basicConfig(level=logging.INFO, filename= "logs/log.log", format=('%(message)s'))

def log(device, message):
    logging.info(f"{datetime.now().isoformat()} [{device}] {message}")