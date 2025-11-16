# Desenvolva uma lógica que leia o peso e a altura de uma pessoa , calcule seu *IMC* e mostre seu status, de acordo com a tabela abaixo :
# - abaixo de 18.5 : abaixo do peso 
# - entre 18.5 e 25 : peso ideial 
# - 25 e 30 sobrepeso 
# - 30 até 40 obesidade 
# - acima de 40 obesidade mórbida 

alt = float(input('Coloque sua altura em metros : '))
peso = float(input('Coloque seu peso : '))

imc = peso / (alt **2)

if imc < 18.5 :
    print(f'O seu resultado foi de {imc:.2f}, ele indica Abaixo do peso')
elif imc <= 24.9 :
    print(f'O seu resultado foi de {imc:.2f}, ele indica Peso ideal')
elif imc <= 29.9 :
    print(f'O seu resultado foi de {imc:.2f}, ele indica Sobrepeso')
elif imc <= 40 :
    print(f'O seu resultado foi de {imc:.2f}, ele indica Obesidade')
else : 
    print(f'O seu resultado foi de {imc:.2f}, ele indica Obesidade Morbida')
