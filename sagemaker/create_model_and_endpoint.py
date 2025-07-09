import sagemaker
from sagemaker.sklearn.model import SKLearnModel
import boto3

bucket = 'weather-forecast-model-bucket'  
model_artifact = f's3://{bucket}/model.tar.gz'


sagemaker_session = sagemaker.Session()
role = "arn:aws:iam::109249930734:role/weather-sagemaker-execution-role"

model = SKLearnModel(
    model_data=model_artifact,
    role=role,
    entry_point='inference.py',
    source_dir='code',
    framework_version='1.2-1',  
    sagemaker_session=sagemaker_session
)


predictor = model.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.large',
    endpoint_name='weather-forecast-endpoint'
)
