def istherespace(string):
    if string.count(' '):
        return f'Seu nome tem {string.count(' ')} espaços'
    return 'Seu nome não espaços'


nome = input('Digite seu nome: ').strip()
idade = input('Digite sua idade: ')
if len(nome) != 0 and len(idade) != 0:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    print(istherespace(nome))
    print(f'Seu nome tem {len(nome.replace(' ', ''))} letras')
    print(f'A primeira letra do sue nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
else:
    print('Um ou mais Campos vazios!')