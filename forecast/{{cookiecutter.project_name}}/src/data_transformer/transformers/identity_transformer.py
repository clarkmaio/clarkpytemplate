

from src.data_transformer.transformers.transformer import Transformer


class IdentityTransformer(Transformer):

    def transform(self, X, train: bool = False):
        return X