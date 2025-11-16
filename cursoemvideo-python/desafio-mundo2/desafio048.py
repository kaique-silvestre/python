# Faça um programa que calcule a soma entre todos os números impares que são mutiplos de três e que se encontram no intervalo de 1 até 500

cont = 0 
im = 0
for im in range(1, 500, 2) :
    if im % 3 == 0 :
        cont += im 
print(cont)

# não sei como somar os valores do intervalo em uma variavél contadora 
# Aprendi como somar os valores em uma variável contadora
# Atualizei o código para ele ser mais eficiente, como aprendi no último vídeo, agora ele é duas vezes mais rapido do que era. 