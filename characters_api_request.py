import requests
import hashlib
import time
from keys import public_key, private_key

public_key = public_key
private_key = private_key
timestamp = str(int(time.time()))
hash_value = hashlib.md5((timestamp + private_key + public_key).encode('utf-8')).hexdigest()

base_url = "http://gateway.marvel.com/v1/public/characters"
params = {
    'ts': timestamp,
    'apikey': public_key,
    'hash': hash_value,
    'limit': 100  # Ajusta según tus necesidades
}

all_characters_data = []

offset = 0
while True:
    params['offset'] = offset

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code != 200:
        print(f"Error en la solicitud: {response.status_code}")
        print(response.text)
        break

    characters_data = data['data']['results']
    all_characters_data.extend(characters_data)

    if len(characters_data) < params['limit']:
        # Si la cantidad de resultados es menor que el límite, hemos llegado al final
        break

    offset += params['limit']

# Ahora 'all_characters_data' contiene la información de todos los personajes
for character in all_characters_data:
    print(f"Nombre: {character['name']}, Descripción: {character['description']}")