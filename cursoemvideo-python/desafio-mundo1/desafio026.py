# Faça um programa que leia uma frase pelo teclado e mostre : 
# • Quantas vezes aparecem a letras "A"
# • Em que posição ela aparece a primeira vez 
# • Em que posição ela aparece a ultima vez 

frase = str(input('Escreva uma frase : ')).strip().upper().replace(' ', '')
print(frase.count('A'))
print(frase.find('A')+1)
print(frase.rfind('A')+1)

