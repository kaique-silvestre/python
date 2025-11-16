# Escreva um programa na tela que leia dois números inteiros e compare-os, mostrando na tela uma mensagem :
# O primeiro valor é maior 
# O segundo valor é maior 
# Não existe valor maior, os dois são iguais 

primeiro = int(input('Coloque o primeiro número inteiro : '))
segundo = int(input('Coloque o segundo número inteiro : '))
if primeiro > segundo :
    print('O primeiro valor é maior')
elif segundo > primeiro :
    print('O segundo valor é maior')
elif primeiro == segundo :
    print('Os valores são iguais')
else : 
    print('Houve algúm erro, tente novamente')
