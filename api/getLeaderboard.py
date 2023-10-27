import boto3
import json

def getLeaderboard():
    # sort by totalBadges and then by completedAllAt
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('csjProgress')
    response = table.scan(
        ProjectionExpression='userid, totalBadges, completedAllAt',
        FilterExpression='totalBadges > :zero',
        ExpressionAttributeValues={
            ':zero': '0'
        },
        Sort = ['totalBadges', 'completedAllAt'],
        Limit=1000,
    )
    response = response['Items']
    return response

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps(getLeaderboard())
    }

print(lambda_handler(0,0)['body'])