
from prefect.logging import get_logger
import logging
import os
from typing import Dict


def setup_logger(log_file_name: str, log_config: Dict):

    # If you are not using Prefect logger (fool!) switch the comment hash of the following two lines

    logger = get_logger() # Prefect logger
    #logger = logging.getLogger(__file__) # Standard logger

    if 'console' in log_config:
        logger.setLevel(level=log_config['console']['level'])

    if 'file' in log_config:
        filename = os.path.join(log_config['file']['filepath'], log_file_name)
        fileHandler = logging.FileHandler(filename=filename)
        fileHandler.setLevel(level=log_config['file']['level'])
        formatter = logging.Formatter(log_config['file']['format'])
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)


    return logger