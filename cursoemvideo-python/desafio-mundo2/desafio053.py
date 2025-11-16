# Faça um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

print('ATENÇÃO NÃO USE PONTUAÇÃO, NEM ACENTUAÇÃO')
p = str(input('Verificador de palíndromos : ')).strip().replace(' ', '').lower()

if p == p[::-1] :
    print(f'É um palíndromo')
else :
    print('Não é um palíndromo')

# Poderia usar diversos .replace() para trocar todas as vogais acentuadas, traços e pontuação na língua portuguesa, não são tantos e o programa iria funcionar muito melhor 
