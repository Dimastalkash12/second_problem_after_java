from db import Leagues
import requests
import json

url = 'https://v3.football.api-sports.io/leagues'
headers = {"x-apisports-key": "330758c4f9d6b00a73af59708b090e4d"}

response = requests.get(url, headers=headers)
response.raise_for_status()

data = response.json()
if data.get("errors"):
    raise RuntimeError(f"API error: {data['errors']}")
leagues = data["response"]
with open("output.json",'r',encoding='utf-8') as file:
    json1=json.loads(file.read())
for i in json1:
    print(i['league']['name'],i['league']['id'])