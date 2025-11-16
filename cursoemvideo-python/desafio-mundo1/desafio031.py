# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas 
print('Vamos calcular o valor da sua viagem, cobrando 0,50 centavos para viagens de até 200km e 0,45 centavos para vaiegsn maiores')
kmh = int(input('Insira a distancia da viagem : '))  
if kmh > 200 : 
    taxa1 = 0.45  
    print(f'O valor total da sua viagem é R${kmh * taxa1}')
else : 
    taxa2 = 0.50 
    print(f'O valor total da sua viagem é R${kmh * taxa2}')