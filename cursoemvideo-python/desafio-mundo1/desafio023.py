# faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. 
# Ex - digite um número : 1834
# unidade : 4
# dezenas : 3
# centenas : 8
# milhar : 1 

num = int(input('insira qualquer número inteiro : '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Unidade : {u}')
print(f'Dezena : {d}')
print(f'Centena : {c}')
print(f'Milhar : {m}')