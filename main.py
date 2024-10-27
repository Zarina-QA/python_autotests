import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'token'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
BODY = {
    "name": "Бульбазавр",
    "photo_id": 143
}
BODY_smena = {
    "pokemon_id": "79081",
    "name": "New Name",
    "photo_id": 2
}
BODY_ohota = {
    "pokemon_id": "79081"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY)
print(response_create.text)

response_smena = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_smena)
print(response_smena.text)

response_ohota = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_ohota)
print(response_ohota.text)
