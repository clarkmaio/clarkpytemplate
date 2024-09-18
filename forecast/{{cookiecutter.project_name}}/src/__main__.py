
import os
import yaml
from prefect import flow
from datetime import datetime
from time import time
from clarkpy_essentials import ParserManager, Context, DataCatalog

from src.pipeline.train import TrainPipeline
from src.log import setup_logger

@flow(name='main')
def main(context: Context):

    start_time = time()
    context.logger.info('Program started')

    if context.parser['mode'] == 'train':
        TrainPipeline(context = context)
    elif context.parser['mode'] == 'predict':
        raise NotImplementedError()
    elif context.parser['mode'] == 'backtest':
        raise NotImplementedError()
    else:
        raise NotImplementedError(f"Unknown mode {context.parser['mode']}")

    end_time = time()
    context.logger.info(f'Program terminated - {(end_time - start_time):.1f}')

    return




if __name__ == '__main__':


    SOURCE_PATH = os.getcwd()

    # ---------------------- DEFINE CONTEXT ----------------------
    # Load parser
    PARSER_PATH = os.path.join(SOURCE_PATH, 'conf', 'parser.yml')
    parser_args = ParserManager.load(path=PARSER_PATH)
    
    # Load config
    CONFIG_PATH = os.path.join(SOURCE_PATH, 'conf', 'config.yml')
    config = yaml.safe_load(open(CONFIG_PATH, 'r'))

    # Load data catalog
    DATA_CATALOG_PATH = os.path.join(SOURCE_PATH, 'conf', 'catalog.yml')
    catalog = DataCatalog(catalog=DATA_CATALOG_PATH, source_path = SOURCE_PATH)

    # Setup logger
    log_file_name = f"{datetime.now().strftime('%Y%m%d_%H%M')}_test.log"
    logger = setup_logger(log_file_name=log_file_name, log_config=config['log'])

    context = Context(parser=parser_args, config = config, catalog=catalog, logger=logger)


    # ---------------------- START PROGRAM ----------------------
    main(context=context)
