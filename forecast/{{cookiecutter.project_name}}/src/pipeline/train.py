

from prefect import task
from clarkpy_essentials  import Context, Pipeline, Node

from src.data_loader.data_loader import load_X_y
from src.model.model_hub import model_hub
from src.nodes.data_processing import transform_data

@task(name='train_pipeline')
def TrainPipeline(context: Context):

    pipeline = Pipeline([
        Node(func=load_X_y, 
             inputs=None,
             outputs='data'),

        Node(func=train_models,
             inputs=['data', 'context'],
             outputs=None)
        
    ])

    pipeline.run(context=context)



def train_models(data, context):
    for model_name in context.parser['model']:
        model, model_cfg = model_hub(model_name=model_name, context=context)
    
        steps = model_cfg['data_transformer']
        X, y = transform_data(data=data, steps=steps, train=True)
        
        model.fit(X=X, y=y)
