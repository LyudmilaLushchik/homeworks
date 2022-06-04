import requests


class Superhero:

    def __init__(self, name):
        self.name = name
        self.get_attributes()

    def __lt__(self, other):
        return self.intelligence < other.intelligence

    def __str__(self):
        return self.name

    def get_attributes(self):
        resp = requests.get('https://superheroapi.com/api/2619421814940190/search/' + self.name)

        if 'success' in resp.json().get('response'):
            res = resp.json()['results']
            for item in res:
                if item['name'] == self.name:
                    self.id = item['id']
                    self.intelligence = int(item['powerstats']['intelligence'])
            return True
        else:
            return False

def get_name_smartest(heroes_list):
        superheroes_list = [Superhero(i) for i in heroes_list if Superhero(i).get_attributes()!=False]
        smartest = superheroes_list[0]
        for hero in (superheroes_list[1:]):
            if smartest.__lt__(hero):
                smartest = hero
        return f'Супергерой {smartest}, id {smartest.id}, самый умный из перечисленных!'
print(get_name_smartest(['Hulk', 'Captain America', 'Thanos']))