import boto3
import json
import time
from boto3.dynamodb.conditions import Attr

def getLeaderboard():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('csjProgress')
    response = table.scan(
        ProjectionExpression='userid, userName, totalBadges, completedAllAt',
    )
    response = response['Items']
    # sort by totalBadges and then by completedAllAt
    print("sorting now")
    response = sorted(response, key=lambda i: (i['totalBadges'], -i['completedAllAt']), reverse=True)

    for i in range(len(response)):
        response[i]['completedAllAt'] = int(response[i]['completedAllAt'])
        response[i]['totalBadges'] = int(response[i]['totalBadges'])

    return response

def postToS3(data):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('csjprogress')
    name = f'leaderboard.json'
    bucket.put_object(
        Key=name,
        Body=json.dumps(data),
        ContentType='application/json'
    )
    return name

def lambda_handler(event, context):
    data = getLeaderboard()
    url = f'https://csjprogress.s3.ap-south-1.amazonaws.com/{postToS3(data)}'
    return {
        'statusCode': 200,
        'body': json.dumps({
            'url': url
        })
    }

print(lambda_handler(0,0)['body'])