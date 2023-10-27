import requests
from bs4 import BeautifulSoup
import json
import time
import boto3

# url = 'https://www.cloudskillsboost.google/public_profiles/a58a9c90-1728-44ef-9012-3910ceff0192'


def updateDynamoDB(data):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('csjProgress')
    response = table.put_item(
        Item=data
    )
    return response

def fetchBadges(id):
    url = f'https://www.cloudskillsboost.google/public_profiles/{id}'

    allowedbadges = ['Google Cloud Computing Foundations: Cloud Computing Fundamentals',
    'Google Cloud Computing Foundations: Infrastructure in Google Cloud',
    'Google Cloud Computing Foundations: Networking & Security in Google Cloud',
    'Google Cloud Computing Foundations: Data, ML, and AI in Google Cloud',
    'Create and Manage Cloud Resources',
    'Perform Foundational Infrastructure Tasks in Google Cloud',
    'Build and Secure Networks in Google Cloud',
    'Perform Foundational Data, ML, and AI Tasks in Google Cloud',
    'Introduction to Generative AI',
    'Level 3 GenAI: Prompt Engineering']

    response = requests.get(url).content

    soup = BeautifulSoup(response, 'html.parser')
    allBadges = soup.find_all('div', {"class": "profile-badge"})

    badges = []
    count = 0
    for i in allBadges:
        i = i.find_all('span')
        i = {
            "name": i[0].text.strip(),
            "completedAt": i[1].text.strip(),
        }
        badges.append(i)
        count += 1

    return badges, count

def lambda_handler(event, context):
    id = event['Records'][0]['body']
    badges, count = fetchBadges(id)
    response = {
        "userid": id,
        "totalBadges": str(count),
        "lastUpdated": str(int(time.time())),
        "completedQuests": badges
    }
    if count > 9:
        response['completedAllAt'] = str(int(time.time()))
    else:
        response['completedAllAt'] = '0'
    updateDynamoDB(response)
    return {
        'statusCode': 200,
        'body': json.dumps('DynamoDB Updated')
    }
lambda_handler({"Records": [{"body": "a58a9c90-1728-44ef-9012-3910ceff0192"}]}, None)