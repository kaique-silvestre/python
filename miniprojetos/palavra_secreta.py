from random import choice
from os import system
palavra_secreta = choice(['banana', 'uva', 'tentativa', 'casa', 'numero', 'escolha', 'musica', 'vontade', 'palhaço', 'morte', 'cavaleiros', 'queijo', 'zinco', 'filme', 'plural', 'nome', 'pessoa', 'animal', 'pai', 'arte', 'jogo', 'sentimento', 'ilha', 'poço', 'choque', 'laranja', 'dormir', 'noite', 'sono', 'porta', 'baralho', 'rato', 'ouro', 'perfume'])

tentativas = 0

lista_secreta = list()
lista_publica = list()

for c in palavra_secreta:
    lista_secreta.append(c)
    lista_publica.append('*')


print(f"Palavra Secreta: {len(palavra_secreta) * '*'}")
try:
    while lista_publica != lista_secreta:
        
        letra = input('Letra: ')

        if len(letra) != 1:
            print('Por favor, digite apenas uma letra.')
            continue
        if letra.isdigit():
            print('Por favor, digite apenas letras')
            continue

        tentativas += 1
        if letra in lista_secreta:
            f = 0
            for linha in lista_secreta:
                if linha == letra:
                    lista_publica[f] = letra
                f+=1
            for linha in lista_publica:
                print(linha, end='')
            print()
        else:
            print('*')
    # system('cls')
    print('PARABÉNS, VOCÊ GANHOU')
    print(f'Tentativas: {tentativas}')
    print(f'Palavra secreta: {palavra_secreta}')
except Exception as erro:
    print(f'Desculpe. Houve algum erro, tente novamente... Classe do Erro: {erro, erro.__class__}')