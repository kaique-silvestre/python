# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento 
# Para salários superiores a R$1.250, calcule um aumento de 10% 
# Para inferiores ou iguais o aumento é de 15% 

salario = float(input('Coloque o valor do seu Salário : '))
if salario >= 1251 : 
    print(salario + (salario * 0.10))
else : 
    print(salario + (salario * 0.15))