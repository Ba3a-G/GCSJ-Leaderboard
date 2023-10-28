import boto3
import json

def cleanData():
    #read line by line
    with open('data.txt', 'r') as f:
        data = f.readlines()
    #clean data
    data = [i.strip() for i in data]
    data = [i.split('/')[4] for i in data]
    return data

def lambda_handler(event, context):
    #push all ids to sqs
    ids = cleanData()
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='updateProgress')
    for id in ids:
        queue.send_message(MessageBody=id)
    return {
        'statusCode': 200,
        'body': json.dumps('All profiles queued for update')
    }

print(lambda_handler(0,0)['body'])