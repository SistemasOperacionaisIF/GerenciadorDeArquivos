from models.gerenciador_arquivos import GerenciadorArquivos


def iniciar_terminal():
    gerenciador = GerenciadorArquivos()

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
        elif comando[0] == "exit":
            break
        else:
            print("Comando inválido")