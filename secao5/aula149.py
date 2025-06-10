class MyContextManager:
    def __init__(self, camaninho_arquivo, modo, encoding='UTF-8'):
        # Como estamos criando um Context Manager é importante definirmso o construtor da com um arquivo e um dos modos do mesmo.  
        self.caminho_arquivo = camaninho_arquivo
        self.modo = modo
        self.encoding = encoding
        self._arquivo = None

    def __enter__(self):
        print("ABRINDO ARQUIVO")
        self._arquivo =  open(self.caminho_arquivo, self.modo, encoding=self.encoding)
        return self._arquivo 
        
    def __exit__(self, class_excepetion, excepetion_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()


# instancia = MyContextManager()

with MyContextManager('aula149.txt', 'w') as var: # Método __enter__ joga uma variável em var
    print('WITH')
    print(var) # enter não joga nada na variável, por isso é None