# Criando Context Manager com um @Decorator

from contextlib import contextmanager

@contextmanager
def MyContextManager(caminho_arquivo, modo):
    try:
        print("Abrindo Arquivo")
        arquivo = open(caminho_arquivo, modo, encoding='UTF-8')
        yield arquivo
    except Exception as error:
        print('Ocorreu erro: ', error)
    finally: 
        # Usando o finally, independente se houver ou não algum erro, o arquivo será fechado no final.
        arquivo.close()

with MyContextManager("aula150.txt", "W") as arquivo:
    arquivo.write("Linha1\n")
    arquivo.write("Linha2\n")
    arquivo.write("Linha3\n")

