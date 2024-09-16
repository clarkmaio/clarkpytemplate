
from abc import abstractmethod

class Transformer:

    @abstractmethod
    def transform(self, X, train: bool = False):
        raise NotImplementedError('Missing transform method')