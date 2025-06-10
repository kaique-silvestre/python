# Operadores úteis

set1 = {1, 2, 3}
set2 = {2, 3, 4}

# União | União - une ambos sets (.union()) 
set3 = set1 | set2 
print(set3)
# output >>> {1, 2, 3, 4}

# intersecção & intersecção - itens presentes em ambos sets (.intersection())
set4 = set1 & set2
print(set4)
# output >>> {2, 3}

# difrença - difrença -- itens presentes aepnas no set da esquerda (.difference())
set5 = set1 - set2
print(set5)
# output >>> {1}

# diferença simetrica ^ diferença simetrica - itens que não estão em ambos sets (.symmetric_difference()) 
set6 = set1 ^ set2
print(set6)
# output >>> {1, 4}