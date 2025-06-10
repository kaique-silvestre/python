
# Criando arquivo no modo de escrita
arquivo = open('aula116\\primeiro_texto.txt', 'w', encoding='utf-8')

arquivo.write('Primeiro texto escrita dentro da manipulação de arquivo\n')

arquivo.close()

# Abrindo arquivo no modo de adição ao fianl
arquivo = open('aula116\\primeiro_texto.txt', 'a', encoding='utf-8')

arquivo.write('Escrevendo a segunda linha com o arquivo aberto no modo de adição de texto ao final')

arquivo.close()

# Abrindo e lendo conteúdo do arquivo
arquivo = open('aula116\\primeiro_texto.txt', 'r', encoding='utf-8')

print(arquivo.read())

arquivo.close()