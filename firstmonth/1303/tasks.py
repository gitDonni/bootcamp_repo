import requests
from pprint import pprint


data = requests.get('https://rickandmortyapi.com/api/character/')

data = data.json()

pprint(f'Bсего персонажей - {data["info"]["count"]} штук')

counter = 1

while True:
    data = requests.get(f'https://rickandmortyapi.com/api/character?page={counter}').json()
    for i in data['results']:
        pprint(i['name'])
    choice = input('n/p - ')
    if choice == 'n':
        counter += 1
    elif choice == 'p':
        counter -= 1
    elif choice == 'e':
        break