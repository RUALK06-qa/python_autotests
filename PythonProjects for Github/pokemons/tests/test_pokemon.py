import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2/'

def test_status_code():
    response = requests.get(url = f'{URL}trainers', params = {'city': 'Moscow'})
    assert response.status_code == 200

def test_name():
    response = requests.get(url = f'{URL}trainers', params = {"trainer_id": 408})
    assert response.json() ['data'] [0] ['trainer_name'] == 'Timofey'