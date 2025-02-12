class Usuario:
    def __init__(self, nome, tipo="comum"):
        self.nome = nome
        self.tipo = tipo
    
    def __str__(self):
        return f"{self.nome} ({self.tipo})"
