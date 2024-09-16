
import pandas as pd
import numpy as np
from prefect import task

@task
def return_features() -> pd.DataFrame:
    return pd.DataFrame(np.random.randn(1000, 5))