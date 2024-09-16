
from typing import Tuple
from prefect import task

from clarkpy_essentials import Context


@task
def model_hub(model_name: str, context: Context) -> Tuple:

    if model_name == 'LinearRegression':
        from sklearn.linear_model import LinearRegression
        model_cfg = context.catalog(f'{model_name}Conf')
        model = LinearRegression(**model_cfg['default_params'])
        return model, model_cfg
    else:
        raise ValueError(f'Unknown model {model_name}')
