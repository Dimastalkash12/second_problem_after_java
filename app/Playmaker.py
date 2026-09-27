class Playmaker:
    def __init__(self,data):
        self.name = data['response'][0]['player']['name']
        self.lastname = data['response'][0]['player']['lastname']
        self.age = data['response'][0]['player']['age']
        self.birth = data['response'][0]['player']['birth']
        self.nationality = data['response'][0]['player']['nationality']
        self.height = data['response'][0]['player']['height']
        self.weight = data['response'][0]['player']['weight']
        self.photo = data['response'][0]['player']['photo']
        self.statistics = data['response'][0]['statistics']

