def executa(funcao, *args):
    return funcao(*args)


print(
    executa(lambda x, y: x + y, 5, 5)
)