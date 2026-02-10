turmas = {}
alunos = {}
presencas = []
notas = []

# ===== FUNÇÕES DE VALIDAÇÃO =====
def input_numerico(mensagem):
    while True:
        valor = input(mensagem)
        if valor.isdigit():
            return valor
        print("Digite apenas números!\n")

def input_texto(mensagem):
    while True:
        valor = input(mensagem)
        if valor.replace(" ", "").isalpha():
            return valor
        print("Digite apenas letras!\n")

# ===== CADASTRAR TURMA =====
def cadastrar_turma():
    id_turma = input_numerico("ID da turma: ")

    if id_turma in turmas:
        print("ID da turma já cadastrado!\n")
        return

    professor = input_texto("Professor: ")

    turmas[id_turma] = {
        "professor": professor
    }
    print("Turma cadastrada com sucesso!\n")

# ===== CADASTRAR ALUNO =====
def cadastrar_aluno():
    nome = input_texto("Nome do aluno: ")
    id_aluno = input_numerico("ID do aluno: ")

    if id_aluno in alunos:
        print("ID do aluno já cadastrado!\n")
        return

    id_turma = input_numerico("ID da turma: ")

    if id_turma not in turmas:
        print("Turma não existe!\n")
        return

    alunos[id_aluno] = {
        "nome": nome,
        "turma": id_turma
    }
    print("Aluno cadastrado com sucesso!\n")

# ===== EDITAR ALUNO =====
def editar_aluno():
    id_aluno = input_numerico("Digite o ID do aluno que deseja editar: ")

    if id_aluno not in alunos:
        print("Aluno não cadastrado!\n")
        return

    print(f"\nAluno atual: {alunos[id_aluno]['nome']}")
    print("1 - Editar nome")
    print("2 - Editar turma")
    print("3 - Editar nome e turma")

    opcao = input_numerico("Escolha uma opção: ")

    if opcao == "1":
        novo_nome = input_texto("Novo nome: ")
        alunos[id_aluno]["nome"] = novo_nome

    elif opcao == "2":
        nova_turma = input_numerico("Novo ID da turma: ")
        if nova_turma not in turmas:
            print("Turma não existe!\n")
            return
        alunos[id_aluno]["turma"] = nova_turma

    elif opcao == "3":
        novo_nome = input_texto("Novo nome: ")
        nova_turma = input_numerico("Novo ID da turma: ")
        if nova_turma not in turmas:
            print("Turma não existe!\n")
            return
        alunos[id_aluno]["nome"] = novo_nome
        alunos[id_aluno]["turma"] = nova_turma

    else:
        print("Opção inválida!\n")
        return

    print("Aluno editado com sucesso!\n")

# ===== REGISTRAR PRESENÇA OU FALTA =====
def registrar_presenca_ou_falta():
    id_aluno = input_numerico("ID do aluno: ")

    if id_aluno not in alunos:
        print("Aluno não cadastrado!\n")
        return

    while True:
        data = input("Data (dd/mm): ")
        if len(data) == 5 and data[2] == "/" and data[:2].isdigit() and data[3:].isdigit():
            dia = int(data[:2])
            mes = int(data[3:])
            if 1 <= dia <= 31 and 1 <= mes <= 12:
                break
        print("Data inválida!\n")

    presente = input("O aluno esteve presente? (s/n): ").lower() == "s"

    tipo_falta = None
    if not presente:
        print("1 - Justificada")
        print("2 - Injustificada")
        print("3 - Disciplinar")
        opcao = input_numerico("Escolha: ")

        if opcao == "1":
            tipo_falta = "justificada"
        elif opcao == "2":
            tipo_falta = "injustificada"
        elif opcao == "3":
            tipo_falta = "disciplinar"
        else:
            print("Tipo inválido!\n")
            return

    presencas.append({
        "aluno": id_aluno,
        "data": data,
        "presente": presente,
        "tipo_falta": tipo_falta
    })
    print("Registro concluído!\n")

# ===== REGISTRAR NOTA =====
def registrar_nota():
    id_aluno = input_numerico("ID do aluno: ")

    if id_aluno not in alunos:
        print("Aluno não cadastrado!\n")
        return

    materia = input_texto("Matéria: ")

    while True:
        try:
            nota = float(input("Nota (0 a 100): "))
            if 0 <= nota <= 100:
                break
        except ValueError:
            pass
        print("Nota inválida!\n")

    notas.append({
        "aluno": id_aluno,
        "materia": materia,
        "nota": nota
    })
    print("Nota registrada!\n")

# ===== RELATÓRIO =====
def relatorio_faltas_aluno():
    id_aluno = input_numerico("ID do aluno: ")

    if id_aluno not in alunos:
        print("Aluno não cadastrado!\n")
        return

    soma = qtd = 0

    for n in notas:
        if n["aluno"] == id_aluno:
            soma += n["nota"]
            qtd += 1

    media = soma / qtd if qtd > 0 else 0

    print("\nAluno:", alunos[id_aluno]["nome"])
    print(f"Média: {media:.2f}\n")

# ===== MENU =====
def menu():
    while True:
        print("=== GESTOR DE TURMAS ===")
        print("1 - Cadastrar turma")
        print("2 - Cadastrar aluno")
        print("3 - Editar aluno")
        print("4 - Registrar presença/falta")
        print("5 - Registrar nota")
        print("6 - Relatório do aluno")
        print("0 - Sair")

        opcao = input_numerico("Escolha: ")

        if opcao == "1":
            cadastrar_turma()
        elif opcao == "2":
            cadastrar_aluno()
        elif opcao == "3":
            editar_aluno()
        elif opcao == "4":
            registrar_presenca_ou_falta()
        elif opcao == "5":
            registrar_nota()
        elif opcao == "6":
            relatorio_faltas_aluno()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!\n")

menu()
