# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão 


a1 = int(input('Primeiro termo da PA: '))
rz = int(input('Razão da PA: '))
cont = 0

for pa in range(a1, 100000, rz):
    cont += 1
    if cont < 11:
        print(pa)

# admito que precisei tirar dúvidas com o chatgpt para entender esse exercício, não estava compreendendo a lógica de como fazer com que apenas os 10 primeiros valores aparecessem, apesar de entender a lógica da PA 
# Sendo que mais uma vez a falha principal foi na falta de conhecimento em relação ao conceito de variável acumualadora 