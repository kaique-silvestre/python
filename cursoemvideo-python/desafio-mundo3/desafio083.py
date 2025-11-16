# Crie um programa onde um usuario digite uma expressão qualquer que use parênteses. Seu plicativo devrá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta 

exp = str(input('Exp: '))
p1 = exp.count('(')
p2 = exp.count(')')
p3 = p1 + p2
if p1 == 0 or p2 == 0:
    print('Está incorreto')
elif p3 % 2 == 0:
    print('Os parenteses estão corretos')
else: 
    print('Os parenteses estão errados')


# Ver se existe uma forma  se saber se existe uma quantidade par de parenteses, dessa forma eu sei que todos os parenteses foram fechados corretamente 