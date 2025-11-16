import requests
from bs4 import BeautifulSoup

url = 'http://localhost:8000/'
response = requests.get(url) # Request GET da URL
response_html = response.text # Pappsando apenas o texto para uma var 
html = BeautifulSoup(response_html, 'html.parser', from_encoding='utf-8') # Por meio da BeautifulSoup transformando o HTML em obj python

#Também hpa o parâmetro 'from_econding' para definirmos o enconding do obj BEuatifulSoup

print(html.title)


# Usando seletores para achar uma parte do texto
## Função .select_one, mostra apenas um seletor
print(html.select_one("#intro > div > div > article > h2"))


# Selecionando elemento "acima" com atributo .parent 
## Nesse caso selecionando o article que estava acima do H2 
print(html.select_one("#intro > div > div > article > h2"))