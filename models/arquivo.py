import random


class Arquivo:
    def __init__(self, nome, tamanho, armazenamento, conteudo=""):
        self.nome = nome
        self.conteudo = conteudo
        self.blocos = armazenamento.alocar_indexada(tamanho)
        self.tamanho = tamanho if tamanho else random.randint(10, 100)

    def visualizar(self):
        print(f"📄 Conteúdo do arquivo '{self.nome}':")
        print(self.conteudo if self.conteudo else "[Arquivo vazio]")

    def editar(self, novo_conteudo):
        self.conteudo = novo_conteudo
        print(f"✏️ Arquivo '{self.nome}' foi editado com sucesso!")