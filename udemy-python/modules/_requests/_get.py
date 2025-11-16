import requests
from pprint import pprint

API_KEY = "53f00f08b6f48ce30a9b814d9d8f472e8ce3d728fd159583621b3e98c623ccf1"

# Pegar informações - GET
response = requests.get(f"https://economia.awesomeapi.com.br/json/last/USD-BRL?token={API_KEY}")

##Transformando a resposta pra JSON para que seja um DICT vizualizavel
response_json = response.json()

pprint(response_json['USDBRL'])