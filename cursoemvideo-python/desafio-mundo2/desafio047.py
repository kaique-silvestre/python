# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

for s in range(1, 51):
    if s%2 == 0 :
        print(s)

# Após a aula do guanabara eu aprendi que apesar do meu método estar certo, ele não é o mais eficiênte, já que da forma em que eu escrevi o código o processador :
# 1) Irá passar por todos os números de 1 a 50. 
# 2) Irá dividir todos os números e verificar o resto da divisão deles
# 3) Para só então confirmar se ele irá exibir ou não na tela
# Obviamente que com a quantidade de dados que eu estou trabalhando, isso não faz diferença nenhuma entretanto, se fosse um sistema enorme, como o de uma empresa e mais pesado, qualquer economia faz a difrença
# O método seguinte feito pelo guanabara é 2x mais eficiente

for s in range(2, 51, 2):
    print(s) 

# Nesse método, o intervalo não irá processar todos os números de 1 a 50, apenas a metade deles, já que o salto de pulo é de 2 em 2
# E ele também faz sentido para o caso dos números pares pois eles já são conhecidos.
# A formula mais simples para descobrir quais números são pares não é dividi-los por 2 e verificar o resto e sim pular de 2 em dois 
# Não há exceção, não há regras diferentes e nem surpresas, todos os números de 2 em 2 são pares
# portanto esse metodo tem o dobro de eficiencia e sua aplicação faz total sentido
# Por isso é importante se lembrar que a simplicidade é a forma mais alta de sofisticação