import os 

# Junta os caminhos conforme o OS 
## Veja que em um MAc ou Linux o sentido das barras ao printar seria outro

path_01 = os.path.join('\\Users', 'kaiqu', 'Desktop', 'biblioteca', 'file.txt')
print(path_01)


# Divide o caminho do arquivo 
path_02 = os.path.split(path_01)
print(path_02)


# Retorna se o caminho selecionado existe com um bool 
IsThisReal = os.path.exists('C:\\Users\\kaiqu\\Desktop\\biblioteca\\python\\udemy-python')
print(IsThisReal, end='\n')

# Retorna o caminho absoluto 
# Se colocar como parâmetro um pornto: '.', será retornado o caminho absoluto da pasta atual
abspath = os.path.abspath('.')
print(abspath)

# o nome base é a parte final 
basename = os.path.basename(abspath)
print(basename)

#dirname 
# pega o caminho do nome do diretorio 
dirname = os.path.dirname(abspath)
print(dirname)
