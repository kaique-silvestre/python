# Crie um pequeno sietma modularizado que permite cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter duas opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas. 


import libi
import arquivo


arq = 'cursoemvideo.txt'

if arquivo.arquivoExiste(arq):
    print('Arquivo encontrando com sucesso')
else:
    print('Arquivo não encontrado')
    arquivo.criarArquivo(arq)

while True:
    reposta = libi.menu(['Ver pessoas Cadastradas', 'Cadastrar Nova pessoa', 'Sair do sistema'])
    if reposta == 1:
        lerArquivo(arq)
    elif reposta == 2:
        arquivo.cabeçalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = libi.LeiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif reposta == 3:
        print('saindo do sistema')
        break
    else:
        print('ERRO. tente Novamente.')