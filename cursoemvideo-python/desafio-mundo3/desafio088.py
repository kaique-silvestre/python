# Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta

from random import sample

x = list(range(1, 60))
prov = list()

j = int(input('Quantos jogos devem ser sorteados: '))
q = int(input('Quantidade de números que cada jogo deve ter: '))
for i in range(0, j):
    y = (sample(x, q))
    prov.append(y)
    print(f'{i+1}º jogo é: {y}')
print('Cadastramento do sorteio em uma lista: ')
print('=-'*30)
print(prov)