
import pandas as pd
import numpy as np
from prefect import task

@task
def return_target() -> pd.Series:
    return pd.Series(np.random.randn(1000))