import requests

response = requests.get("https://python-api-a70a6-default-rtdb.firebaseio.com/.json")

print(response.json())

# POST
# Criar informação
## Parametro: link e data

dados = '{"Nome": "Anderson", "Sobrenome": "Mello"}'
new_response = requests.post("https://python-api-a70a6-default-rtdb.firebaseio.com/.json", data=dados)

print(new_response)

