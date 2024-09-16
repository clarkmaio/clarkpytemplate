

from typing import Tuple
import pandas as pd
from prefect import task
from src.data_loader.features import return_features
from src.data_loader.target import return_target

@task
def load_X_y() -> pd.DataFrame:
        X, y = return_features(), return_target()
        data = pd.concat([X, y.to_frame('target')], axis=1)
        return data

