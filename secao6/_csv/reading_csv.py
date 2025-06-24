import pathlib
import csv

# Camimnho do arquivo 
csv_path = pathlib.Path(__file__).parent / 'data_example.csv'

# Abrir arquivo CSV 
with open(csv_path, 'r', encoding='UTF-8') as file:
    # Leitura do CSV passando valores pra variável
    data = csv.reader(file)

    # Leitura de linha por linha da variável 
    # Caso não seja visto pleo for usar (next)
    for line in data:
        print(line)

print()

# Abrir e ler arquivo como um dicionário A
with open(csv_path, 'r', encoding='UTF-8') as file:
    values = csv.DictReader(file)

    for item in values:
        print(item) 