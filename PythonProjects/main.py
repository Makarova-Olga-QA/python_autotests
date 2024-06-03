import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'bd5a182efcf1eb48ee8fa6cb8fc25aff'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "olka8156@mail.ru",
    "password": "MOG08111996"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create  = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
body_rename = {
    "pokemon_id": "27048",
    "name": "Felix",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
body_catch = {
    "pokemon_id": "27048"
}


'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''message = response_create.json()['message']
print(message)'''

'''response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)'''

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)




