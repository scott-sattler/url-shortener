import boto3
db = boto3.client('dynamodb', region_name='local', endpoint_url='http://localhost:8000', use_ssl=False, aws_access_key_id='fakeMyKeyId', aws_secret_access_key='fakeSecretAccessKey', verify=False)
print(db.list_tables())

