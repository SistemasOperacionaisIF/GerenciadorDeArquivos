import random
from models.arquivo import Arquivo
from models.diretorio import Diretorio
from models.armazenamento import Armazenamento


class GerenciadorArquivos:
    def __init__(self):
        self.raiz = Diretorio("root")
        self.atual = self.raiz  # Diretório onde o usuário está no momento
        self.armazenamento = Armazenamento(1000)  # Inicializa o armazenamento com 1000 KB

    def mudar_diretorio(self, nome):
        if nome == "..":  # Voltar um nível
            self.atual = self.raiz
        elif nome in self.atual.conteudo and isinstance(self.atual.conteudo[nome], Diretorio):
            self.atual = self.atual.conteudo[nome]
        else:
            print("Diretório não encontrado")
    
    def criar_arquivo(self, nome):
        tamanho = random.randint(10, 100)  # Tamanho aleatório
        if self.armazenamento.pode_alocar(tamanho):
            self.atual.adicionar(nome, Arquivo(nome, tamanho=tamanho))
            self.armazenamento.alocar(tamanho)
            print(f"Arquivo '{nome}' criado com {tamanho} KB.")
        else:
            print("Espaço insuficiente no armazenamento!")

    def criar_diretorio(self, nome):
        if nome in self.atual.conteudo:
            print("Já existe um diretório com esse nome!")
        else:
            self.atual.adicionar(nome, Diretorio(nome))

    def listar_conteudo(self):
        for nome in self.atual.conteudo:
            print(f"[DIR] {nome}" if isinstance(self.atual.conteudo[nome], Diretorio) else f"[ARQ] {nome}")

    def mostrar_armazenamento(self):
        print(f"Espaço usado: {self.armazenamento.espaco_usado} KB / {self.armazenamento.tamanho_total} KB")

    def visualizar_arquivo(self, nome):
        if nome in self.atual.conteudo:
            arquivo = self.atual.conteudo[nome]
            if isinstance(arquivo, Arquivo):
                arquivo.visualizar()
            else:
                print(f"'{nome}' não é um arquivo.")
        else:
            print(f"Arquivo '{nome}' não encontrado.")

    def editar_arquivo(self, nome, novo_conteudo):
        if nome in self.atual.conteudo:
            arquivo = self.atual.conteudo[nome]
            if isinstance(arquivo, Arquivo):
                arquivo.editar(novo_conteudo)
            else:
                print(f"'{nome}' não é um arquivo.")
        else:
            print(f"Arquivo '{nome}' não encontrado.")


    def deletar(self, nome):
        if nome in self.atual.conteudo:
            obj = self.atual.conteudo[nome]
        
            # Se for um arquivo, pode ser removido normalmente
            if isinstance(obj, Arquivo):
                self.armazenamento.liberar(obj.tamanho)
                self.atual.remover(nome)
                print(f"'{nome}' foi deletado e liberou {obj.tamanho} KB.")
        
        # Se for um diretório, verificar se está vazio
            elif isinstance(obj, Diretorio):
                if not obj.conteudo:  # Diretório está vazio
                    self.atual.remover(nome)
                    print(f"Diretório '{nome}' foi removido.")
                else:
                    print(f"Erro: Diretório '{nome}' não está vazio.")
        else:
            print("Arquivo ou diretório não encontrado.")
