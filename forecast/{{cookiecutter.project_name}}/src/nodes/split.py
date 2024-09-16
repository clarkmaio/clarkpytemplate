
import pandas as pd
from prefect import task
from typing import Tuple

@task(name='split_X_y')
def split_X_y(data: pd.DataFrame, target_column: str = 'norm_actuals', exclude_columns_from_X: list = ['norm_actuals', 'actuals', 'capacity', 'dispatch']) -> Tuple[pd.DataFrame, pd.Series]:
    '''
    Split data into X, y to feed scikit like models
    '''
    assert target_column in data.columns, f'{target_column} not found in data columns'

    X = data.drop(columns=exclude_columns_from_X, errors='ignore')
    y = data[target_column]

    # Remove target column from X just to be sure
    X = X.drop(columns=target_column, errors='ignore')

    return X, y
