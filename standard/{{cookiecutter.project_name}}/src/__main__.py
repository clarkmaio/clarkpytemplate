
import os
import yaml
from typing import Dict
from prefect import flow
from prefect.logging import get_logger
import logging
from datetime import datetime

from settings_manager.parser_manager import ParserManager
from settings_manager.settings_catalog import SettingsCatalog
from orchestrator.test.pipeline import TestPipeline



# TODO REFACTORING
def setup_logger(log_file_name: str, log_config: Dict):
    logger = get_logger()


    # console
    logger.setLevel(level=log_config['level'])


    # file handler
    fileHandler = logging.FileHandler(filename=f'/home/clarkmaio/Scrivania/{log_file_name}')
    fileHandler.setLevel(level=log_config['level'])
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)


    return logger


@flow(name='main')
def main(settings: SettingsCatalog):

    if settings.parser['mode'] == 'test':
        TestPipeline(settings = settings)
    else:
        raise NotImplementedError(f"Unknown mode {settings.parser['mode']}")

    return






if __name__ == '__main__':

    # Load parser
    PARSER_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'conf', 'parser.yml')
    parser_args = ParserManager.load(path=PARSER_PATH)
    
    # Load config file
    CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'conf', 'config.yml')
    config = yaml.safe_load(open(CONFIG_PATH, 'r'))

    # Set logger
    log_file_name = f"{datetime.now().strftime('%Y%m%d_%H%M')}_test.log"
    _ = setup_logger(log_file_name=log_file_name, log_config=config['log'])
    
    settings_catalog = SettingsCatalog(parser=parser_args, config = config)
    main(settings=settings_catalog)
