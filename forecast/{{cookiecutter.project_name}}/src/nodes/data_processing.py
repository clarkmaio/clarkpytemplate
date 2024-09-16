
from typing import List
from prefect import task

from src.data_transformer import DataTransformer
from src.nodes.split import split_X_y

@task
def transform_data(data, steps: List, train: bool = False):
    
    data_transformer = DataTransformer(steps=steps)
    processed_data = data_transformer.transform(X=data, train=train)

    X, y = split_X_y(data=processed_data, target_column='target')
    return X, y 