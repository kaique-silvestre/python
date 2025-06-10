def greeting(greet):
    def togreet(name):
        return f'{greet}, {name}'
    return togreet

goodmorning = greeting('Good Morning')
goodnight = greeting('Good Morning')


print(goodmorning('Madalena'))
print(goodnight('Beatriz'))

for name in ['Mario', 'Helder', 'Helena', 'Maria', 'Bianca']:
    print(goodmorning(name))