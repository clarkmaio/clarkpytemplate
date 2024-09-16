
import os
import yaml
from typing import Dict
from prefect import flow
from prefect.logging import get_logger
import logging
from datetime import datetime
from pathlib import Path

from clarkpy_essentials import ParserManager, Context, DataCatalog

from src.pipeline.train import TrainPipeline



# TODO REFACTORING
def setup_logger(log_file_name: str, log_config: Dict):
    logger = get_logger()

    # Console handler
    logger.setLevel(level=log_config['level'])

    # file handler
    filename = os.path.join(log_config['filepath'], log_file_name)
    fileHandler = logging.FileHandler(filename=filename)
    fileHandler.setLevel(level=log_config['level'])
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)


    return logger


@flow(name='main')
def main(context: Context):

    if context.parser['mode'] == 'train':
        TrainPipeline(context = context)
    elif context.parser['mode'] == 'predict':
        raise NotImplementedError()
    elif context.parser['mode'] == 'backtest':
        raise NotImplementedError()
    else:
        raise NotImplementedError(f"Unknown mode {context.parser['mode']}")

    return






if __name__ == '__main__':


    SOURCE_PATH = os.getcwd()

    # Load parser
    PARSER_PATH = os.path.join(SOURCE_PATH, 'conf', 'parser.yml')
    parser_args = ParserManager.load(path=PARSER_PATH)
    
    # Load config file
    CONFIG_PATH = os.path.join(SOURCE_PATH, 'conf', 'config.yml')
    config = yaml.safe_load(open(CONFIG_PATH, 'r'))

    # Load data catalg
    DATA_CATALOG_PATH = os.path.join(SOURCE_PATH, 'conf', 'catalog.yml')
    catalog = DataCatalog(catalog=DATA_CATALOG_PATH, source_path = SOURCE_PATH)

    # Set logger
    log_file_name = f"{datetime.now().strftime('%Y%m%d_%H%M')}_test.log"
    _ = setup_logger(log_file_name=log_file_name, log_config=config['log'])
    
    context = Context(parser=parser_args, config = config, catalog=catalog)
    main(context=context)
