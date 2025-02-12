class Armazenamento:
    def __init__(self, tamanho_total=1000, tamanho_bloco=10):
        self.tamanho_total = tamanho_total
        self.tamanho_bloco = tamanho_bloco
        self.blocos_livres = list(range(tamanho_total // tamanho_bloco))  # Lista de blocos livres

    @property
    def espaco_usado(self):
        return (self.tamanho_total // self.tamanho_bloco - len(self.blocos_livres)) * self.tamanho_bloco

    def alocar_indexado(self, tamanho):
        num_blocos = (tamanho + self.tamanho_bloco - 1) // self.tamanho_bloco  # Arredonda para cima
        if len(self.blocos_livres) >= num_blocos:
            alocados = self.blocos_livres[:num_blocos]
            del self.blocos_livres[:num_blocos]
            return alocados
        else:
            print("Erro: Espaço insuficiente!")
            return []

    def liberar(self, blocos):
        self.blocos_livres.extend(blocos)
