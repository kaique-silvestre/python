"""
Lista que me permite:
     fazer() - Adicionar itens
        - Listar itens em um arquivo separado  
     desfazer() - Tirar os itens adicionados 
     Refazer() - Voltar com os itens desfeitos
     Listar() - Mostrar itens a fazer
"""   
import function
from os import system
from time import sleep
import json


def add(todo_list): ###
    syscls()
    item = ''
    print("Add each of the itens you have to do")
    print("to stop write 'break'\n")
    while True:
        try:
            item = str(input('- ')).strip()
            if item.lower() == 'break':
                break
            if not item:
                raise Exception
            todo_list.append(item)
        except Exception as erro:
            print('Invalid Input! Try again.')
            print(erro.__class__)

def to_list(list_to_list, list_name): ###
    syscls()
    if empty(list_to_list) == True:
        print("\nNothing to see here\n")
        return True 
    print(f"That's your '{list_name}' list\n")
    for item in list_to_list:
        print('-', item)
    print('\n')

def delete(list_to_delete):
    syscls()
    print()
    if empty(list_to_delete):
        print('\nThere\' Nothing to Delete\n')
        return True
    while True:
        try:
            print('Wich Item you want to delete? type -1 to end\n')
            for index, item in enumerate(list_to_delete):
                print(index, '-', item)
            print()
            deleted = int(input('Write the number: '))
            if deleted == -1:
                break
            deleted_item = todo_list.pop(deleted)
            trash(deleted_item, trash_list)
            print(f'\nitem \'{deleted_item}\' was deleted from the list\n')
        except Exception as erro:
            print("\nInvalid Input! Try again.\n")
            continue

def restore_trash(restore_from, restore_to):
    syscls()
    if empty(trash_list):
        print('\nNothing in the trash\n')
        return True
    print('\nWich item do want to restore? to end type: -1\n')
    opt = ''
    while True:
        try:
            for index, item in enumerate(trash_list):
                print(index, '-', item)
            opt = int(input('\nWrite the Number: '))
            print('\n')
            if opt == -1:
                break
            item_to_restore = trash_list.pop(opt)
            restore_to.append(item_to_restore)
        except Exception as erro:
            print("\nInvalid Input! Try again\n")

def quick_delete(list_to_delete):
    syscls()
    if empty(list_to_delete):
        print('\nNothing to delete\n')
        return 0
    deleted_item = list_to_delete.pop()
    trash(deleted_item, trash_list)
    print(f'item \'{deleted_item}\' was deleted')


def trash(garbage, trash_list):
    trash_list.append(garbage)
    
def empty(array):
    if len(array) == 0:
        return True
 
def syscls():
    system('cls')

def isavalidindex(array, index):
    if index <= len(array):
        return True
    return False   

def save_file(array):
    with open('./todo_list.json', 'w+', encoding='utf-8') as archeive:
        json.dump(array, archeive)

todo_list = ['one', 'two', 'three', 'four']
trash_list = []

while True:
    print('''To [A]dd / [L]ist / [D]elete / [Q]uick Delete / [R]estore / [T]rash''')
    opt = str(input('Option: \t')).upper()
    if opt == 'A':
        add(todo_list)
    elif opt == 'L':
        to_list(todo_list, 'to do')
    elif opt == 'D':
        delete(todo_list)
    elif opt == 'R':
        restore_trash(trash_list, todo_list)
    elif opt == 'T':
        to_list(trash_list, 'Trash')
    elif opt == 'Q':
        quick_delete(todo_list)
    elif opt == 'S':
        save_file(todo_list)
    else:
        print("\nChose a valid option\n")
        continue
       