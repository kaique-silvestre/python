import requests

link = "https://python-api-a70a6-default-rtdb.firebaseio.com/-OTnPhDnV0EFfXr3EXoA/.json"

new_data = '{"Nome": "Jose", "Sobrenome": "Melo"}'
# Patch
## Recebe como parâmetros: Link e data a ser adicionado
response = requests.patch(link, data=new_data)

print(response)

print(requests.get(link).json())