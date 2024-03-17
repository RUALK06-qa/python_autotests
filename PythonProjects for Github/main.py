import requests 

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type' : 'application/json'}
TOKEN = 'token'
body = {
    "trainer_token": TOKEN,
    "email": "e-mail",
    "password": "password" }
body_confirm = {
     "trainer_token": TOKEN

}

response = requests.post(url=f'{URL}/trainers/reg', headers = HEADERS, json = body)
print(response.text)

response_confirm = requests.post(url=f'{URL}/trainers/confirm_email', headers = HEADERS, json = body_confirm)
print(response_confirm.text)