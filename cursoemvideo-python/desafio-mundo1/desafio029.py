# Escreva um programa que leia a velocidade de um carro. 
# Se ela ultrapassar 80Km/h, mostre uma mensagem  dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite 

multa = 7
limite = 80 

velocidade = int(input('Coloque a velocidade : '))

if velocidade > limite : 
    formula = (velocidade - limite) * multa
    print(f'Você foi multado por exceder a velocidade máxima oermitida, o valor da sua multa é R${formula}')
else : 
    print('Tudo nos conformes, dirija com segurança!!!')