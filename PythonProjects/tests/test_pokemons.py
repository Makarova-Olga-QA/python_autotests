import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'bd5a182efcf1eb48ee8fa6cb8fc25aff'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '4238'

def test_status_code():
    responce = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert responce.status_code == 200

def test_get_trainer_by_id():
    responce = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert responce.json()["data"][0]["trainer_name"] == 'Олька'






