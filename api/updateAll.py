import boto3
import json
from boto3.dynamodb.conditions import Attr

def fetchAllIds():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('csjProgress')
    response = table.scan(
        ProjectionExpression='userid',
        FilterExpression=Attr('totalBadges').lt(9)
    )
    response = response['Items']
    return response

def lambda_handler(event, context):
    #push all ids to sqs
    ids = fetchAllIds()
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='updateProgress')
    for id in ids:
        queue.send_message(MessageBody=id['userid'])
    return {
        'statusCode': 200,
        'body': json.dumps('All profiles queued for update')
    }

print(lambda_handler(0,0)['body'])