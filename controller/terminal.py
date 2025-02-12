from models.gerenciador_arquivos import GerenciadorArquivos
from models.usuario import Usuario


def iniciar_terminal():
    print("🔐 Bem-vindo ao sistema de arquivos!")
    
    nome_usuario = input("Nome de usuário: ").strip()
    tipo_usuario = input("Tipo de usuário (admin/comum): ").strip().lower()
    
    if tipo_usuario not in ["admin", "comum"]:
        print("Tipo inválido! Definindo como usuário comum.")
        tipo_usuario = "comum"
    
    usuario = Usuario(nome_usuario, tipo_usuario)
    gerenciador = GerenciadorArquivos(usuario)

    print(f"✅ Usuário autenticado: {usuario}\n")

    while True:
        gerenciador.mostrar_armazenamento()

        comando = input(f"{gerenciador.atual.nome} $ ").strip().split()

        if not comando:
            continue
        elif comando[0] == "ls":
            gerenciador.listar_conteudo()
        elif comando[0] == "cd" and len(comando) > 1:
            gerenciador.mudar_diretorio(comando[1])
        elif comando[0] == "mkdir" and len(comando) > 1:
            gerenciador.criar_diretorio(comando[1])
        elif comando[0] == "touch" and len(comando) > 1:
            gerenciador.criar_arquivo(comando[1])
        elif comando[0] == "rm" and len(comando) > 1:
            gerenciador.deletar(comando[1])
        elif comando[0] == "view" and len(comando) > 1:
            gerenciador.visualizar_arquivo(comando[1])
        elif comando[0] == "nano":
            if len(comando) < 3:
                print("Uso correto: nano <arquivo> <novo conteúdo>")
            else:
                nome_arquivo = comando[1]
                novo_conteudo = " ".join(comando[2:])
                gerenciador.editar_arquivo(nome_arquivo, novo_conteudo)
        elif comando[0] == "exit":
            break
        else:
            print("Comando inválido")
