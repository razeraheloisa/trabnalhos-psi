nomes = []

def validar_nome(nome):
    nome = ' '.join(nome.split())

    if len(nome) < 2:
        print("Erro: O nome deve ter pelo menos 2 caracteres.")
        return None

    if not nome.replace(" ", "").isalpha():
        print("Erro: O nome não pode conter números ou símbolos.")
        return None

    return nome

def adicionar_nome():
    nome = input("Digite o nome: ")
    nome = validar_nome(nome)
    if not nome:
        return

    if nome.lower() in [n.lower() for n in nomes]:
        print("Nome já cadastrado.")
        return

    nomes.append(nome)
    print(f"Nome '{nome}' adicionado com sucesso!")

def listar_nomes():
    if not nomes:
        print("Nenhum nome cadastrado.")
        return

    print("Lista de nomes em ordem alfabética:")
    for i, nome in enumerate(sorted(nomes, key=str.lower)):
        print(f"{i} - {nome}")

def buscar_nome():
    busca = input("Digite o nome para buscar: ").lower()
    encontrado = False

    for i, nome in enumerate(nomes):
        if nome.lower() == busca:
            print(f"Encontrado: {nome} (posição {i})")
            encontrado = True

    if not encontrado:
        print("Nome não encontrado.")

def remover_nome():
    nome = input("Digite o nome para remover: ").lower()

    for n in nomes:
        if n.lower() == nome:
            confirmacao = input(f"Tem certeza que deseja remover '{n}'? (s/n): ").lower()
            if confirmacao == "s":
                nomes.remove(n)
                print(f"Nome '{n}' removido com sucesso!")
            else:
                print("Remoção cancelada.")
            return

    print("Nome não encontrado.")

def editar_nome():
    antigo = input("Digite o nome que deseja editar: ").lower()

    for i, nome in enumerate(nomes):
        if nome.lower() == antigo:
            novo = input("Digite o novo nome: ")
            novo = validar_nome(novo)
            if not novo:
                return

            if novo.lower() in [n.lower() for n in nomes]:
                print("Esse nome já existe.")
                return

            nomes[i] = novo
            print(f"Nome '{nome}' editado para '{novo}' com sucesso!")
            return

    print("Nome não encontrado.")

def ordenar_nomes():
    if not nomes:
        print("Nenhum nome para ordenar.")
        return

    print("Nomes em ordem alfabética:")
    for nome in sorted(nomes, key=str.lower):
        print("-", nome)

def contar_nomes():
    print(f"Total de nomes cadastrados: {len(nomes)}")

def apagar_todos_nomes():
    confirmacao = input("Tem certeza que deseja apagar todos os nomes? (s/n): ").lower()
    if confirmacao == "s":
        nomes.clear()
        print("Todos os nomes foram apagados!")
    else:
        print("Ação cancelada.")

while True:
    print("\n=== GESTOR DE NOMES ===")
    print("1 - Adicionar nome")
    print("2 - Listar nomes")
    print("3 - Buscar nome")
    print("4 - Remover nome")
    print("5 - Editar nome")
    print("6 - Ordenar nomes")
    print("7 - Contar nomes")
    print("8 - Apagar todos os nomes")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_nome()
    elif opcao == "2":
        listar_nomes()
    elif opcao == "3":
        buscar_nome()
    elif opcao == "4":
        remover_nome()
    elif opcao == "5":
        editar_nome()
    elif opcao == "6":
        ordenar_nomes()
    elif opcao == "7":
        contar_nomes()
    elif opcao == "8":
        apagar_todos_nomes()
    elif opcao == "0":
        print("Obrigado por usar o Gestor de Nomes")
        break
    else:
        print("Opção inválida.")
