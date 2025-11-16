n1 = int(input('digíte um valor: '))
n2 = int(input('Digíte outro número: '))
s = n1 + n2 
m = n1 * n2 
d = n1 / n2 
di = n1 // n2 
r = n1 % n2 
print('Os valores {} e {}, tem sua soma de {}, seu produto de {}, sua divisão de {}'.format(n1, n2, s, m, d) end='')
print('sua divisão inteira é {} e o resto da sua divisão inteira é {}'.format(di, r))