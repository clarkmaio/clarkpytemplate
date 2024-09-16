


from ..transformers.transformer import Transformer


class DropnaTransformer(Transformer):

    def __init__(self, subset_train: list = None,  
                 subset_predict: list = None, 
                 except_train: list = None, 
                 except_predict: list = None):
        self.subset_train = subset_train
        self.subset_predict = subset_predict
        self.except_train = except_train
        self.except_predict = except_predict


    def transform(self, X, train: bool = False):

        # Decide what to drop depending if you are training
        col_to_drop = self.subset_train if train else self.subset_predict
        col_not_to_drop = self.except_train if train else self.except_predict

        if col_to_drop is None:
            if col_not_to_drop is None:
                X_tranform = X.dropna(how='any')
            else:
                col_to_drop = [col for col in X.columns if col not in col_not_to_drop]
                X_tranform = X.dropna(subset=col_to_drop)
        else:
            X_tranform = X.dropna(subset=col_to_drop)

        return X_tranform