# desenvolva um programa que leia seis números interios e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.
# Comentario : Mais uma vez acredito que minha solução não é a mais sofisticada, ansioso para ver como guanabara vai resolver 

num1 = int(input('Coloque o primeiro valor: '))
num2 = int(input('Coloque o segundo valor: '))
num3 = int(input('Coloque o terceiro valor: '))
num4 = int(input('Coloque o quarto valor: '))
num5 = int(input('Coloque o quinto valor: '))
num6 = int(input('Coloque o sexto valor: '))

cont = 0
if num1 % 2 == 0 : 
    cont += num1 
if num2 % 2 == 0 : 
    cont += num2 
if num3 % 2 == 0 : 
    cont += num3 
if num4 % 2 == 0 : 
    cont += num4 
if num5 % 2 == 0 : 
    cont += num5 
if num6 % 2 == 0 : 
    cont += num6 
print(f'A soma de todos os números pares digítados é : {cont}')

# Devido ao fato de eu não ter entendido muito bem o conceito de variável acumuladora, eu fiz esse exercicio igual um homem da caverna, ou seja tudo de forma rustica, digitando todos os códigos em muitas linhas 
# Agora eu entendi bem o conceito, consigo refazer com mais tarnquilidade, so que teria que refazer todos os seguintes kkkkkkkkkkkkkkkkkkkkkkkk
# Minha maior duvida foi: Como usar o laço for, se eu preciso guardar os valores para poder somar ? acho que por essa conclusão cheguei nessa forma tão rústica de se fazer, duvida essa minha que foi preenchida pela variável acumualadora, pois realmente, sem elas os input não teriam como ser salvos para serem somados, então já que minha duvida era justamente messa questão especifica faz sentido eu ter escolhido essa forma para fazer 
