import requests
class League:
    def __init__(self,apiKey):
        self.apiKey=apiKey

    def viewAll(self,hiders):
        response = requests.get("https://v3.football.api-sports.io/leagues", headers=hiders)
        data = response.json()
        leagues={}
        for league in data["response"]:
                leagues[league["league"]["id"]]=league['league']['name']+' '+league['country']['name']
        return leagues