# faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário, O programa será interrompido quando o número solicitato for negativo  
print('-='*30)
print('PROGRAMA DA TABOADA')
print('Coloque qualquer número negativo para encerrar')
while True:
    print('-='*30)
    n = int(input('Número: '))
    if n <= 0 :
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')
print('CONEXÃO FINALIZADA')