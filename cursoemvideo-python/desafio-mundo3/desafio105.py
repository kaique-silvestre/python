# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quanidade de notas 
# - A maior nota 
# - A menor nota
# - A média da turma 
# - Situação ( opcional ) = acima de 7 boa, 6 = razoavel 4 = ruim 
# Adcione também as docstrings a função 

def notas(a, b=True):
    info = dict()
    info['Quantidade de notas'] = len(a)
    info['A maior nota'] = max(a)
    info['A menor nota'] = min(a)
    info['Média'] = sum(a)/len(a)
    if b == True:
        if info['Média'] >= 7:
            info['Situação'] = 'boa'
        elif info['Média'] >= 5:
            info['Situação'] = 'Razoavel'
        else:
            info['Situação'] = 'Ruim'
    return info

pro = list()

while True:
    a = int(input('Várias notas: '))
    if a == 0:
        break
    pro.append(a)
print(notas(pro))


        