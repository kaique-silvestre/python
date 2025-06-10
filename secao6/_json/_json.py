import json 
import os

# json.dumps()
# Convert a python object in json string format 

#Exemple 01
python_string = 'That\'s a string'

json_string = json.dumps(python_string)

print(json_string) # "That's a string"


# Exemple 02
python_dictionary = {'Name': 'Charles', 'Age': 1500}

json_object = json.dumps(python_dictionary, indent=4, sort_keys=True)

print(json_object) # {"Name": "Charles", "Age": 1500}
print(type(json_object)) # <class 'str'>


# json.dump

file_path = os.path.abspath('.')

print(file_path)

file_path = os.path.join(file_path, '_json', 'jsonFile.json')

# print(os.path.exists(file_path))

if os.path.exists(file_path):
    with open(file_path, 'w+', encoding='utf8') as file:
        python_dict = {
            'Account': 1003,
            'Name': 'Jonh',
            'Last_Name': 'Mcdonald',
            'Balance': 100_000.25,
            'Ocupation': None
        }
        json.dump(python_dict, file, indent=True)