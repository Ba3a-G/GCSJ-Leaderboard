import boto3
import time

def dumpDatabase():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('csjProgress')
    response = table.scan()
    return response['Items']

def postToS3(data):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('csjProgress')
    name = f'csjProgress{str(int(time.time()))}.json'
    bucket.put_object(
        Key=name,
        Body=json.dumps(data)
    )
    return name