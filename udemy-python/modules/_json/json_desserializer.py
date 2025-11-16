# json.loads 
## Desserialiação uma string json em um dict python

import json
import os 

string_python = "That\'s a string"

json_string = json.dumps(string_python)

new_python_object = json.loads(json_string)

print(new_python_object)
print(type(new_python_object))

print()

file_path = os.path.abspath('.') 
file_path = os.path.join(file_path, '_json', 'jsonFile.json')

if os.path.exists(file_path):
    with open(file_path, 'r+', encoding='utf8') as file:
        python_obj = json.load(file)
print(python_obj)