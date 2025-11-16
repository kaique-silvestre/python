# Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input(f'Peso da {i}º pessoa em Kg: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'o maior peso é: {maior:.2f}')
print(f'O menor peso é: {menor:.2f}')
   
# Que código lindo!!!!!!!
# Que inteligência magnifica, é realmente uma baita forma de se resolver o problema
# Eu cheguei a pensar na mesma lógica que essa resolução de fazer um conflito a cada validação do intervalo se o peso novo é maior ou menor que o novo peso, eu apenas não sabia como transcrever isso para a sintaxe do python