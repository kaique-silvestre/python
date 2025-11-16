# Faça um programa que tenha uma função chamada area(), que recebe as dimenções de um terreno retangular (largura e comprimento) e mostre a area do terreno

def area(a, b):
    c = a * b
    print(f"A area total é {c}m²")


a = float(input('Largura do terreno (m): '))
b = float(input('Comprimento do terreno (m): '))
area(a, b)
