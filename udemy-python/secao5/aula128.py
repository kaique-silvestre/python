class ContaBancaria:
    taxa_juros = 0.05  # Atributo da classe

    def __init__(self, saldo):
        self.saldo = saldo  # Atributo da instância

    @classmethod
    def alterar_taxa_juros(cls, nova_taxa):
        cls.taxa_juros = nova_taxa  # Modifica o atributo da classe

# Alterando a taxa de juros sem criar uma instância
ContaBancaria.alterar_taxa_juros(0.07)

print(ContaBancaria.taxa_juros)  # Saída: 0.07
