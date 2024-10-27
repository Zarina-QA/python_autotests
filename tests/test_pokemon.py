import requests
import pytest
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '559bd18cbafe5905882d8b4659467e19'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 7266

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_name_of_trainer():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.json()['data'][0]['trainer_name']== 'Зарина'

