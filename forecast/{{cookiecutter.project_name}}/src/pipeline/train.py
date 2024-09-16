

from prefect import task
from clarkpy_essentials  import Context
from src.data_transformer import DataTransformer


from src.data_loader.data_loader import load_X_y
from src.nodes.split import split_X_y
from src.model.model_hub import model_hub
from src.nodes.data_processing import transform_data

@task(name='train_pipeline')
def TrainPipeline(context: Context):
    '''
    Train pipeline:
        1. Load/process data
        2. Initialize model
        3. Train/validation
        4. Save model
    '''

    data = load_X_y()

    for model_name in context.parser['model']:
        model, model_cfg = model_hub(model_name=model_name, context=context)
    
        steps = model_cfg['data_transformer']
        X, y = transform_data(data=data, steps=steps, train=True)
        
        # Fit/validation
        model.fit(X=X, y=y)


    return