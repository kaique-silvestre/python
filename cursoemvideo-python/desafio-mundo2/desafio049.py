# refaça o desafio009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for
 
num = int(input('Escreva um número para saber sua taboada : '))
for c in range(1, 11) :
    print(f'{num} X {c} = {num * c}')
