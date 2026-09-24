import requests
from Playmaker import Playmaker
class Footballers:
    def __init__(self,apiKey):
        self.apiKey=apiKey

    def getPlayer(self,hiders,league,name,season=2024):
        response = requests.get("https://v3.football.api-sports.io/players", headers=hiders,params={'search':name,'league':league,'season':season})
        data = response.json()
        playmaker=Playmaker(data)
        return playmaker
#
#
# footballers=Footballers("330758c4f9d6b00a73af59708b090e4d")
# print(footballers.getPlayer( {"x-apisports-key": '330758c4f9d6b00a73af59708b090e4d'},307,'Cristiano'))
