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
    'Level 3 GenAI: Prompt Engineering']

    response = requests.get(url).content

    soup = BeautifulSoup(response, 'html.parser')
    allBadges = soup.find_all('div', {"class": "profile-badge"})
    userName = soup.find('h1', {"class": "ql-headline-1"}).text.strip()

    badges = []
    count = 0
    for i in allBadges:
        i = i.find_all('span')
        if i[0].text.strip() not in allowedbadges:
            continue
        i = {
            "name": i[0].text.strip(),
            "completedAt": i[1].text.strip(),
        }
        badges.append(i)
        count += 1
    lastBadgeCompletedOn = allBadges[0].find_all('span')[1].text.strip()
    lastBadgeCompletedOn = lastBadgeCompletedOn.split(' ')[2].strip(',')
    return badges, count, userName, lastBadgeCompletedOn

def lambda_handler(event, context):
    id = event['Records'][0]['body']
    badges, count, userName, lastBadgeCompletedOn = fetchBadges(id)
    response = {
        "userid": id,
        "userName": userName,
        "totalBadges": count,
        "lastUpdated": int(time.time()),
        "completedQuests": badges,
        "lastBadgeCompletedOn": lastBadgeCompletedOn
    }
    updateDynamoDB(response)
    return {
        'statusCode': 200,
        'body': json.dumps('DynamoDB Updated')
    }

if __name__ == '__main__':
    lambda_handler({"Records": [{"body": "464c2c97-47ad-4f80-a8e7-b42375e5a665"}]}, None)