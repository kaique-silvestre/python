def mult(*args):
    total = 1
    for num in args:
        total *= num
    return total

valor = mult(7, 2, 10)
print(valor)