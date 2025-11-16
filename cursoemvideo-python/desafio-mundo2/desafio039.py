# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade :
# - Se ele ainda vai precisar se alistar ao serviço militar 
# - Se é a hora de se alistar
# - Se já passou o tempo de alistamento 
# Seu programa também deverá mostrar o tempo que falta ou que já passou do prazo 

from datetime import date
data_atual = date.today().year

nascimento = int(input('Coloque o ano em que nasceu : '))

idade = data_atual - nascimento
idade_de_alistamento = 18

if idade == idade_de_alistamento :
    print('Hora de se alistar!!!')
elif idade < idade_de_alistamento :
    print('Ainda não está na hora de se alistar')
    print(f'Tempo em anos que falta para se alistar : {idade_de_alistamento - idade}')
else : 
    print('Já passou da idade de se alistar')
    print(f'Tempo em anos que já passou desde a idade de se alistar : {(idade_de_alistamento - idade) * -1}')
