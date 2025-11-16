cpf = input("CPF: ").strip()

if '.' and '-' in cpf:
        cpf = cpf.replace('.', '').split('-')
        digitos, validador = cpf
else:
        digitos = cpf[:9]
        validador = cpf[9:]

lista_digitos = list()
mult = 10

for num in digitos:
    lista_digitos.append(mult * int(num))
    mult -= 1

resto = (sum(lista_digitos) * 10) % 11

final1 = 0 if resto > 9 else resto

digitos += str(final1)
lista_digitos.clear()
mult = 11

for num in digitos:
    lista_digitos.append(mult * int(num))
    mult -= 1

resto = (sum(lista_digitos) * 10) % 11

final2 = 0 if resto > 9 else resto

if str(final1) + str(final2) != str(validador):
    print('CPF inválido')
else:
    print('CPF Válido') 
print(final1, final2, validador)