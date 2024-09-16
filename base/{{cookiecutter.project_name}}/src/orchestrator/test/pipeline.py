

from copy import deepcopy
from prefect import task
from prefect.logging import get_logger

from settings_manager.settings_catalog import SettingsCatalog

from .node.test_functions import test_function_1, test_function_2, test_function_3


@task
def TestPipeline(settings: SettingsCatalog):

    logger = get_logger()
    logger.info('This is the test pipeline')

    # Steps of the pipeline
    x = test_function_1(x=settings.config['VAR1'], y=settings.config['VAR2'])
    xx = test_function_2(x=x)
    test_function_3(x=xx)

    return



