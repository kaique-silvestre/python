import pathlib
import os

# Retorno do caminho 
path = pathlib.Path()
abspath = path.absolute() # Caminho Absoluto 
print(abspath) #n C:\Users\kaiqu\Desktop\biblioteca\python\udemy-python

print()

# Retorno do caminho até este arquivo
## A variável especial __file__ nós da o nome do arquivo atual
file_path = pathlib.Path(__file__)
print(file_path)

print()

# Retrono do caminho até o diretório 
path_directory = pathlib.Path(__file__).parent
print(path_directory)


print()

# Retornar home 
print(pathlib.Path.home())

print()

# Criação de arquivos e join de caminhos 
create_path = pathlib.Path.home() / 'Desktop' / 'arquivo.txt'
if not os.path.exists(create_path):
    create_path.touch()
#    ...

# Apagar arquivos
if os.path.exists(create_path):
#    create_path.unlink()
    ...

# Escrever em arquivos 
path_to_write = pathlib.Path.home() / 'Desktop' /'toWrite.txt'
if not os.path.exists(path_to_write):
    path_to_write.touch()
    path_to_write.write_text("i am writing in a file using python and it was create by it")

# Ler um arquivo 
print(path_to_write.read_text())


# Criar uma pasta 


# Remover uma pasta
