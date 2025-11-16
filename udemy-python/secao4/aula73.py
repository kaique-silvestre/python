def greeting(text, name):
    return f'{text}, {name}!'

def execute(function, *args):
    return function(*args)

print(execute(greeting, 'bom dia', 'douglas'))