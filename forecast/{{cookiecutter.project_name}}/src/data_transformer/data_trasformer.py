
from typing import Dict
from dataclasses import dataclass
from copy import deepcopy

from src.data_transformer.transformers.transformer import Transformer
from src.data_transformer.transformers.dropna_transformer import DropnaTransformer

def transformer_hub(step_param: Dict) -> Transformer:

    assert 'type' in step_param, 'Missing type in step_param'

    step_param_tmp = deepcopy(step_param)
    type = step_param_tmp.pop('type')

    if type == 'dropna':
        return DropnaTransformer(**step_param_tmp)
    else:
        raise NotImplementedError(f'Unknown transformer {type}')
    return





@dataclass
class DataTransformer:
    steps: Dict

    def __post_init__(self):
        self._initialize_steps_transformer()

    def _initialize_steps_transformer(self):
        self.steps_transformer = [
            transformer_hub(step_param=step) for step in self.steps
        ]

    def transform(self, X, train: bool = False):
        for step in self.steps_transformer:
            X = step.transform(X, train=train)

        return X
