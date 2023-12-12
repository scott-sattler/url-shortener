import boto3
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
local_endpoint = os.getenv("LOCAL_ENDPOINT")

dynamodb = boto3.resource('dynamodb', endpoint_url=local_endpoint)
try:
    table = dynamodb.create_table(
        TableName='TodoTable',
        KeySchema=[
            {
                'AttributeName': 'itemId',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'itemId',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    print("Table status:", table.table_status)
except Exception as e:
    print('error', e)
