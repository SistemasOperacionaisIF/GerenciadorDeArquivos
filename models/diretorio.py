class Diretorio:
    def __init__(self, nome):
        self.nome = nome
        self.conteudo = {}

    def adicionar(self, nome, obj):
        self.conteudo[nome] = obj

    def remover(self, nome):
        if nome in self.conteudo:
            del self.conteudo[nome]
