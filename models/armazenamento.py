
class Armazenamento:
    def __init__(self, tamanho_total=1000):  # Exemplo: 1000 KB
        self.tamanho_total = tamanho_total
        self.espaco_usado = 0

    def pode_alocar(self, tamanho):
        return self.espaco_usado + tamanho <= self.tamanho_total

    def alocar(self, tamanho):
        if self.pode_alocar(tamanho):
            self.espaco_usado += tamanho
            return True
        return False

    def liberar(self, tamanho):
        self.espaco_usado -= tamanho
