import requests

TOKEN = 'token'

URL = 'https://api.pokemonbattle.me/v2/'

HEADERS_registration = {
    'Content-type': 'application/json'
}

HEADERS_other_requests = {
    'Content-type': 'application/json',
    "trainer_token": "token"
}

body_registration = {
    "trainer_token": "token",
    "email": "e-mail",
    "password": "password"
}

body_name_update = {
    "name": "Timofey",
    "city": "Moscow"
}

'''body_pokemon_creation = {
     "name": "Batonchik",
    "photo": "https://dolnikov.ru/pokemons/albums/058.png"
}'''

body_catch = {
    "pokemon_id": "13961"
}

response_registration = requests.post(url = f'{URL}trainers/reg', headers = HEADERS_registration, json = body_registration)
print(response_registration.text)

response_name_update = requests.put(url = f'{URL}trainers', headers = HEADERS_other_requests, json = body_name_update)
print(response_name_update.text)

'''response_pokemon_creation = requests.post(url = f'{URL}pokemons', headers = HEADERS_other_requests, json = body_pokemon_creation)
print(response_pokemon_creation.text)'''

response_catch = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADERS_other_requests, json = body_catch)
print(response_catch.text)

'''response_list = requests.get(url=f'{URL}trainers', params = {'trainer_id':'408'})
print(response_list.json())'''
