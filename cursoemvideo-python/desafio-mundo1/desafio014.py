# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF
celcius = float(input('informe a temperatura em ºC : '))

print(f'{celcius:.1f}ºC são {((celcius * (9/5)) + 32):.1f}ºF')