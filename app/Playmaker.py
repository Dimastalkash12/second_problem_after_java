

class Playmaker:
    def __init__(self,data):
        self.name=data['response'][0]['player']['name']
        self.lastname=data['response'][0]['player']['lastname']
        self.age=data['response'][0]['player']['age']
        self.birth=data['response'][0]['player']['birth']
        self.nationality=data['response'][0]['player']['nationality']
        self.height=data['response'][0]['player']['height']
        self.weight=data['response'][0]['player']['weight']
        self.photo=data['response'][0]['player']['photo']
        self.statistics=data['response'][0]['statistics']





r={'get': 'players', 'parameters': {'search': 'Cristiano', 'league': '307', 'season': '2024'}, 'errors': [], 'results': 1, 'paging': {'current': 1, 'total': 1}, 'response': [{'player': {'id': 874, 'name': 'Cristiano Ronaldo', 'firstname': 'Cristiano Ronaldo', 'lastname': 'dos Santos Aveiro', 'age': 41, 'birth': {'date': '1985-02-05', 'place': 'Funchal', 'country': 'Portugal'}, 'nationality': 'Portugal', 'height': '187', 'weight': '83', 'injured': False, 'photo': 'https://media.api-sports.io/football/players/874.png'}, 'statistics': [{'team': {'id': 2939, 'name': 'Al-Nassr', 'logo': 'https://media.api-sports.io/football/teams/2939.png'}, 'league': {'id': 307, 'name': 'Pro League', 'country': 'Saudi-Arabia', 'logo': 'https://media.api-sports.io/football/leagues/307.png', 'flag': 'https://media.api-sports.io/flags/sa.svg', 'season': 2024}, 'games': {'appearences': 30, 'lineups': 30, 'minutes': 2625, 'number': None, 'position': 'Forward', 'rating': '7.533333', 'captain': False}, 'substitutes': {'in': 0, 'out': None, 'bench': None}, 'shots': {'total': 113, 'on': 69}, 'goals': {'total': 25, 'conceded': 0, 'assists': 3, 'saves': None}, 'passes': {'total': 787, 'key': 37, 'accuracy': None}, 'tackles': {'total': 6, 'blocks': 2, 'interceptions': 3}, 'duels': {'total': 156, 'won': 68}, 'dribbles': {'attempts': 44, 'success': 17, 'past': None}, 'fouls': {'drawn': 26, 'committed': 9}, 'cards': {'yellow': 2, 'yellowred': None, 'red': 0}, 'penalty': {'won': None, 'commited': None, 'scored': 8, 'missed': 1, 'saved': None}}]}]}
# достать даннные'name': 'Cristiano Ronaldo'lastname': 'dos Santos Aveiro' 'age': 41, 'birth': {'date': '1985-02-05', 'place': 'Funchal', 'country': 'Portugal'} 'nationality': 'Portugal', 'height': '187', 'weight': '83' 'photo': 'https://media.api-sports.io/football/players/874.png'},'statistics': [{'team': 'name': 'Al-Nassr', 'logo': 'https://media.api-sports.io/football/teams/2939.png'}, 'league': 'league' 'name': 'Pro League', 'country': 'Saudi-Arabia', 'logo': 'https://media.api-sports.io/football/leagues/307.png', 'flag': 'https://media.api-sports.io/flags/sa.svg', 'season': 2024}, 'games': {'appearences': 30, 'lineups': 30, 'minutes': 2625, 'number': None, 'position': 'Forward', 'rating': '7.533333', 'captain': False}, 'substitutes': {'in': 0, 'out': None, 'bench': None}, 'shots': {'total': 113, 'on': 69}, 'goals': {'total': 25, 'conceded': 0, 'assists': 3, 'saves': None}, 'passes': {'total': 787, 'key': 37, 'accuracy': None}, 'tackles': {'total': 6, 'blocks': 2, 'interceptions': 3}, 'duels': {'total': 156, 'won': 68}, 'dribbles': {'attempts': 44, 'success': 17, 'past': None}, 'fouls': {'drawn': 26, 'committed': 9}, 'cards': {'yellow': 2, 'yellowred': None, 'red': 0}, 'penalty': {'won': None, 'commited': None, 'scored': 8, 'missed': 1, 'saved': None}
playmaker=Playmaker(r)
