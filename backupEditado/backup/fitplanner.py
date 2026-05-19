import os
os.system('cls' if os.name == 'nt' else 'clear')
# make it work  make it right  make it fast

# >> testar essas funcionalidades:
# criar arquivos importantes! // exercícios - - -

# arquivos = ["cardio.txt", "forca.txt", "flexibilidade.txt", "equilibrio.txt"]
# path = "file/exercicios"
# for nome in arquivos:
#     if not os.path.exists(f"{path}/{nome}"):
#         open(f"{path}/{nome}", "w").close()
# - - - - - - - - - - - - - - -

# [ importante ]
# - ajeitar os 'print()' pra quebra de linha 
# - criar funções da manipulação de arquivos .csv
# - colocar verificação se o arquivo existe ou está vazio
# - falta colocar a visualização e edição dos exercícios // mas eles estão salvos

def menu():
    print("1 - Treinos")
    print("2 - Exercícios")
    print("3 - Metas")
    print("4 - Evolução")
    print("5 - Sugestões")
    print("0 - Sair")
    print()
    opcao = int(input("Insira a opção desejada: "))
    return opcao

def menuTreino():
    print("- - - - TREINOS - - - -")
    print("1 - Novo treino")
    print("2 - Ver treinos")
    print("3 - Editar treino")
    print("4 - Excluir treino")
    print("0 - Voltar")
    print()
    opcao = int(input("> > Opção: "))
    print()
    return opcao

def menuExercicio():
    print("- - - - EXERCÍCIOS - - - -")
    print("1 - Adicionar exercício novo")
    print("2 - Ver exercícios")
    print("3 - Editar")
    print("4 - Excluir exercício")
    print("0 - Voltar")
    print()
    opcao = int(input("> > Opção: "))
    print()
    return opcao

def categoriaExercicio():
    print("- - - Categorias - - -")
    print("1 - Aeróbicos (cardio)")
    print("2 - Força (resistência)")
    print("3 - Flexibilidade/alongamento")
    print("4 - Equilíbrio")
    print("0 - Voltar")
    print()
    categoria = int(input("Selecione uma categoria: "))
    if categoria == 1:
        return "cardio.txt"
    elif categoria == 2:
        return "forca.txt"
    elif categoria == 3:
        return "flexibilidade.txt"
    elif categoria == 4:
        return "equilibrio.txt"
    elif categoria == 0:
        return 0
    else:
        print("\n- Opção inválida -")
        return "invalido"

### Exercícios ###

def atualizarExercicios(path, categoria, listaExercicios):
    arquivo = open(f"{path}/{categoria}", "w")
    for i in range(len(listaExercicios)):
        arquivo.write(f"{listaExercicios[i].strip()}\n")
    arquivo.close()

def addExercicio(path, categoria, exercicios, exercicio):
    exercicios.append(exercicio)
    arquivo = open(f"{path}/{categoria}", "w")
    for i in range(len(exercicios)):
        arquivo.write(f"{exercicios[i].strip()}\n")
    arquivo.close()
    print()
    print(f"[{exercicio}] foi adicionado!")

def abrirExercicios(path, categoria):
    arquivo = open(f"{path}/{categoria}", "r")
    exercicios = arquivo.readlines()
    arquivo.close()
    return exercicios

def listarExercicios(exercicios, categoria):
    if categoria == "cardio.txt":
        print(" > Aeróbicos <")
    elif categoria == "forca.txt":
        print(" > Força <")
    elif categoria == "flexibilidade.txt":
        print(" > Flexibilidade <")
    elif categoria == "equilibrio.txt":
        print(" > Equilíbrio <")

    if len(exercicios) > 0:
        for i in range(len(exercicios)):
            print(f"{i+1} | {exercicios[i].strip()}")
    else:
        print("Sem exercícios cadastrados")

# ------------------------------------------------

# Definir variáveis de treino antes do loop principal
pathTreinos = "files/treinos"
pathExercicios = "files/exercicios"
arquivoTreinos = "treinos.csv"

# Garante que as pastas e arquivos necessários existem antes de usar
def inicializarArquivos():
    os.makedirs(pathTreinos, exist_ok=True)
    os.makedirs(pathExercicios, exist_ok=True)
    for nome in ["cardio.txt", "forca.txt", "flexibilidade.txt", "equilibrio.txt"]:
        caminho = f"{pathExercicios}/{nome}"
        if not os.path.exists(caminho):
            open(caminho, "w").close()

inicializarArquivos()

while True:
    opcaoMenu = menu()

    # - - - - > TREINOS
    if opcaoMenu == 1:
        while True:
            opcaoTreino = menuTreino()

            if opcaoTreino == 1:  # add
                dicionarioTreino = {}

                print("- Adicionar treino novo -")

                
                dicionarioTreino = {
                    'nome':       input("Nome: "),
                    'tipo':       input("Tipo [categoria]: "),
                    'data':       input("Data (dd/mm/aaaa): "),
                    'duracao':    float(input("Duração (em minutos): ")),
                    'objetivo':   input("Objetivo: "),
                    'observacao': input("Observações: "),
                    'exercicios': ""
                }

                print("1 - Sim | 0 - Não")
                opcaoExercicios = int(input("Deseja adicionar exercícios ao seu treino? "))
                if opcaoExercicios == 1:
                    listaExercicios = []
                    while True:
                        tipoExercicio = categoriaExercicio()
                        if tipoExercicio == 0:
                            break
                        exercicios = abrirExercicios(pathExercicios, tipoExercicio)
                        listarExercicios(exercicios, tipoExercicio)
                        if len(exercicios) == 0:
                            print("Cadastre exercícios nessa categoria antes de adicioná-los ao treino.")
                            continue
                        numeroExercicio = int(input("Qual exercício deseja adicionar? "))
                        indiceExercicio = numeroExercicio - 1
                        listaExercicios.append(exercicios[indiceExercicio])
                        print(f"'{exercicios[indiceExercicio].strip()}' foi adicionado ao treino!")

                        print("1 - Sim | 0 - Não")
                        continuar = int(input("Deseja adicionar mais um exercício? "))
                        if continuar == 0:
                            break

                    for i in range(len(listaExercicios)):
                        listaExercicios[i] = listaExercicios[i].strip()
                    exerciciosTreino = "-".join(listaExercicios)
                    dicionarioTreino["exercicios"] = exerciciosTreino

                dicionarioTreino["duracao"] = str(dicionarioTreino["duracao"])
                colunas = ",".join(list(dicionarioTreino.keys())) + "\n"
                dados = ",".join(list(dicionarioTreino.values())) + "\n"

                if os.path.exists(f"{pathTreinos}/{arquivoTreinos}"):
                    arquivo = open(f"{pathTreinos}/{arquivoTreinos}", "a")
                    arquivo.write(dados)
                    arquivo.close()
                else:
                    arquivo = open(f"{pathTreinos}/{arquivoTreinos}", "w")
                    arquivo.write(colunas)
                    arquivo.write(dados)
                    arquivo.close()

                print("Treino salvo!")

            elif opcaoTreino == 2:  # mostrar
                while True:
                    print("- Ver treinos -")

                    if not os.path.exists(f"{pathTreinos}/{arquivoTreinos}"):
                        print("Nenhum treino encontrado.")
                        break

                    arquivo = open(f"{pathTreinos}/{arquivoTreinos}", "r")
                    colunas = arquivo.readline()
                    linhas = arquivo.readlines()
                    arquivo.close()

                    if not linhas:
                        print("Nenhum treino encontrado.")
                        break

                    print("Treinos")
                    for i, linha in enumerate(linhas, start=1):
                        categorias = linha.split(",")
                        print(f"Treino {i} | {categorias[0]}")

                    print(">>> 0 - Sair")

                    formatacao = ["Nome do treino:", "Tipo/Categoria:", "Data:", "Duração:", "Objetivo:", "Observações:"]
                    opcaoVer = int(input("Qual treino deseja visualizar? "))  # [FIX 1] renomeado

                    if 0 < opcaoVer <= len(linhas):
                        linha = linhas[opcaoVer - 1].split(",")
                        print(f"- Treino {opcaoVer} -")
                        for i in range(len(formatacao)):
                            print(f"{formatacao[i]} {linha[i].strip()}")
                    elif opcaoVer == 0:
                        break
                    else:
                        print("Opção inválida.\n")

            elif opcaoTreino == 3:  # editar
                while True:
                    print("- Editar treinos -")
                    if not os.path.exists(f"{pathTreinos}/{arquivoTreinos}"):
                        print("Nenhum treino encontrado.")
                        break

                    arquivo = open(f"{pathTreinos}/{arquivoTreinos}", "r")
                    colunas = arquivo.readline()
                    linhas = arquivo.readlines()
                    arquivo.close()

                    if not linhas:
                        print("Nenhum treino encontrado.")
                        break

                    print("Treinos")
                    for i, linha in enumerate(linhas, start=1):
                        categorias = linha.split(",")
                        print(f"Treino {i} | {categorias[0]}")

                    opcaoEditar = int(input("Qual treino deseja editar? "))
                    if 0 < opcaoEditar <= len(linhas):
                        indiceTreino = opcaoEditar - 1
                        categorias = linhas[indiceTreino].strip().split(",")
                        # [FIX 4] formatação atualizada com 'Data'
                        formatacao = ["Nome do treino:", "Tipo/Categoria:", "Data:", "Duração:", "Objetivo:", "Observações:"]
                        for i in range(len(formatacao)):
                            print(f"{i+1} | {formatacao[i]} {categorias[i]}")

                        print(">>> 0 - Sair")
                        opcaoCategoria = int(input("Qual categoria deseja editar? "))

                        if 0 < opcaoCategoria <= len(formatacao):
                            indiceCategoria = opcaoCategoria - 1
                            novoTexto = input(f"{formatacao[indiceCategoria]} ")
                            categorias[indiceCategoria] = novoTexto
                            categoria_str = ",".join(categorias)
                            linhas[indiceTreino] = categoria_str + "\n"

                            arquivo = open(f"{pathTreinos}/{arquivoTreinos}", "w")
                            arquivo.write(colunas)
                            for i in range(len(linhas)):
                                arquivo.write(linhas[i])
                            arquivo.close()
                        elif opcaoCategoria == 0:
                            break
                        else:
                            print("Opção inválida")

                    elif opcaoEditar == 0:
                        break
                    else:
                        print("Opção inválida.\n")

            elif opcaoTreino == 4:  # excluir
                while True:
                    print("- Excluir arquivo -")

                    if not os.path.exists(f"{pathTreinos}/{arquivoTreinos}"):
                        print("Nenhum treino encontrado.")
                        break

                    arquivo = open(f"{pathTreinos}/{arquivoTreinos}", "r")
                    colunas = arquivo.readline()
                    linhas = arquivo.readlines()
                    arquivo.close()

                    if not linhas:
                        print("Nenhum treino encontrado.")
                        break

                    print("Treinos")
                    for i, linha in enumerate(linhas, start=1):
                        categorias = linha.split(",")
                        print(f"Treino {i} | {categorias[0]}")

                    print(">>> 0 - Sair")
                    opcaoExcluir = int(input("Qual treino deseja excluir? "))

                    if opcaoExcluir == 0:
                        break

                    # [FIX 4] formatação atualizada com 'Data'
                    formatacao = ["Nome do treino:", "Tipo/Categoria:", "Data:", "Duração:", "Objetivo:", "Observações:"]
                    if 0 < opcaoExcluir <= len(linhas):
                        linha = linhas[opcaoExcluir - 1].split(",")
                        print(f"- Treino {opcaoExcluir} -")
                        for i in range(len(formatacao)):
                            print(f"{formatacao[i]} {linha[i].strip()}")
                    else:
                        print("Opção inválida.\n")
                        continue

                    print(f"Tem certeza que deseja apagar o Treino {opcaoExcluir}?")
                    print("1 - Sim | 0 - Não")
                    delete = int(input("[1/0]: "))
                    if delete == 1:
                        indice = opcaoExcluir - 1
                        linhas.pop(indice)
                        arquivo = open(f"{pathTreinos}/{arquivoTreinos}", "w")
                        arquivo.write(colunas)
                        for i in range(len(linhas)):
                            arquivo.write(linhas[i])
                        arquivo.close()
                        print("O Treino foi deletado.")
                    elif delete == 0:
                        print("Cancelado! O arquivo não foi deletado.")
                    else:
                        print("Opção inválida!")

            elif opcaoTreino == 0:
                break

    # - - - - > EXERCÍCIOS
    elif opcaoMenu == 2:
        while True:
            opcaoExercicio = menuExercicio()

            if opcaoExercicio == 1:  # adicionar
                while True:
                    print("- Adicionar exercício novo -")
                    categoria = categoriaExercicio()

                    if categoria == 0:
                        break
                    elif categoria == "invalido":
                        print("Tente novamente ou aperte '0 - Voltar'")
                        continue

                    print()
                    exercicio = input("Nome: ").capitalize()
                    exercicios = abrirExercicios(pathExercicios, categoria)
                    addExercicio(pathExercicios, categoria, exercicios, exercicio)

            elif opcaoExercicio == 2:  # listar
                while True:
                    print("- Ver exercícios -")
                    categoria = categoriaExercicio()

                    if categoria == 0:
                        break
                    elif categoria == "invalido":
                        print("Tente novamente ou aperte '0 - Voltar'")
                        continue

                    exercicios = abrirExercicios(pathExercicios, categoria)
                    listarExercicios(exercicios, categoria)

            elif opcaoExercicio == 3:  # editar
                while True:
                    print("- Editar exercícios -")
                    print("Qual a categoria do exercício que você deseja editar?")
                    categoria = categoriaExercicio()

                    if categoria == 0:
                        break
                    elif categoria == "invalido":
                        print("Tente novamente ou aperte '0 - Voltar'")
                        continue

                    exercicios = abrirExercicios(pathExercicios, categoria)
                    print("Qual exercício deseja editar?")
                    listarExercicios(exercicios, categoria)
                    print()
                    indice = int(input("Exercício nº: ")) - 1
                    novoExercicio = input("Novo texto: ").capitalize()
                    exercicios[indice] = novoExercicio
                    atualizarExercicios(pathExercicios, categoria, exercicios)

            elif opcaoExercicio == 4:  # excluir
                print("- Excluir exercícios -")
                while True:
                    categoria = categoriaExercicio()

                    if categoria == 0:
                        break
                    elif categoria == "invalido":
                        print("Tente novamente ou aperte '0 - Voltar'")
                        continue

                    exercicios = abrirExercicios(pathExercicios, categoria)
                    print("Qual exercício deseja deletar?")
                    listarExercicios(exercicios, categoria)
                    print()
                    indice = int(input("Exercício nº: ")) - 1

                    while True:
                        print(f"Deseja apagar exercício [{exercicios[indice].strip()}]?")
                        confirmacao = int(input("1 - Sim / 0 - Não: "))

                        if confirmacao == 1:
                            exercicios.pop(indice)
                            atualizarExercicios(pathExercicios, categoria, exercicios)
                            print("Exercício deletado!")
                            break
                        elif confirmacao == 0:
                            print("Cancelado!")
                            break
                        else:
                            print("Opção inválida!")
                            continue

            elif opcaoExercicio == 0: 
                break

    elif opcaoMenu == 0:
        print("Saindo...")
        break