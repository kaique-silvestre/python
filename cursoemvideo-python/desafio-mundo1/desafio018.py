# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import radians, sin, cos, tan

ang = int(input('Ângulo : '))
angf = radians(ang)

print(f'O valor do seno é {sin(angf):.2f}, o cosseno {cos(angf):.2f} e a tangente é {tan(angf):.2f}')