# Abrindo com o context manager no modo de escrita
# Se dentro desse bloco for tentado ler, haverá um erro, pois o arquivo não está no modo de leitura  
with open('aula116\\context_manager.txt', 'w', encoding='utf-8') as data:
    data.write('first line\n')
    data.write('second line')

# Abrindo com o context manager no modo de leitura
# Se dentro desse bloco for tentado escrever, haverá um erro, pois o arquivo não está no modo de escrita 
with open('aula116\\context_manager.txt', 'r', encoding='utf-8') as arq:
    print(arq.read())

with open('aula116\\new_archeive.txt', 'w+', encoding='utf-8') as arquivo:
    arquivo.write('w+ permite ler e escrever um arquivo dentro do mesmo gerenciador de contexto\n')
    arquivo.write('Porém sem retornar o cursor para o ponto inicial do arquivo, ele não cosiguirá ler no mesmo context que a escrita')
    print(arquivo.read())
    arquivo.seek(0, 0)
    print(arquivo.read())
