import mlflow.sagemaker as mfs

experiment_id = ''
run_id = ''
region = ''
aws_id = ''
arn = ''
app_name = ''
model_uri = f"mlruns/{experiment_id}/{run_id}/artifacts/random-forest-model"
tag_id = ''

image_url = aws_id + '.dkr.ecr.' + region + '.amazonaws.com/mlflow-pyfunc:' + tag_id

mfs.deploy(app_name,
	model_uri=model_uri,
	region_name=region,
	mode='create',
	execution_role_arn=arn,
	image_url=image_url)