import requests

api_key = 'b16e4f39-5126-425a-b913-6fb1521a187b'
word = 'Potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json() 

for definition in definitions:
    print(definition)