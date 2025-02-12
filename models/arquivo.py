import random


class Arquivo:
    def __init__(self, nome, tamanho ,conteudo=""):
        self.nome = nome
        self.conteudo = conteudo
        self.tamanho = tamanho if tamanho else random.randint(10, 100)

