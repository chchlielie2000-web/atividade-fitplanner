import os
os.system('cls' if os.name == 'nt' else 'clear')
# make it work  make it right  make it fast
# criar arquivos importantes! - - -

# arquivos = ["cardio.txt", "forca.txt", "flexibilidade.txt", "equilibrio.txt"]
# path = "file/exercicios"
# for nome in arquivos:
#     if not os.path.exists(f"{path}/{nome}"):
#         open(f"{path}/{nome}", "w").close()
# - - - - - - - - - - - - - - -

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
    # return categoria
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
        return "invalido" # trocar por inválida

def salvarArquivo(caminho, dicionario, textos): # Salvar como .TXT
    numeroArquivo = len((os.listdir(caminho)))
    
    arquivo = open(f"{caminho}/dados_{numeroArquivo+1}", "w", encoding="utf-8")
    for texto, valor in zip(textos, dicionario.values()):
        arquivo.write(f"{texto}{valor}\n")
    arquivo.close()
    return arquivo

def renomearArquivo(caminho):
    if not os.path.exists("files/treinos"):
        os.makedirs("files/treinos")
    arquivos = sorted(os.listdir(caminho))
    for i, arquivo in enumerate(arquivos, start=1):
        os.rename(f"{caminho}/{arquivo}", f"{caminho}/dados_{i}.txt")
        
def mostrarArquivos(caminho, tipo): # treinos e exercícios
    arquivos = sorted(os.listdir(caminho))
    
    for i in range(len(arquivos)):
        arquivo = open(f"{caminho}/dados_{i+1}.txt", "r")
        nome = arquivo.readline().split()
        print(f"{tipo} {i+1} |", *nome[1:])

def mostrarArquivo(caminho, numArquivo):
    arquivo = open(f"{caminho}/dados_{numArquivo}.txt", "r")
    conteudo = arquivo.read()
    print("- - - - - - - - - - - -")
    print(conteudo.strip())
    print("- - - - - - - - - - - -")

def editarArquivo(caminho, numArquivo, textos):
    arquivo = open(f"{caminho}/dados_{numArquivo}.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()

    print("- - - - -")
    for i, linha in enumerate(linhas, start=1):
        print(f"[{i}] {linha.strip()}")
    print("- - - - -")

    editar = int(input(f"Qual linha deseja editar? [1-{len(linhas)}] "))
    novaLinha = input("Novo texto: ")
    linhas[editar-1] = textos[editar-1]+novaLinha+"\n"

    arquivo = open(f"{caminho}/dados_{numArquivo}.txt", "w")
    arquivo.writelines(linhas)
    arquivo.close()
    
    print("Editado com sucesso!")    
    return arquivo

def apagarArquivo(caminho, numArquivo):
    os.remove(f"{caminho}/dados_{numArquivo}.txt")

### Exercícios ###

def atualizarExercicios(path, categoria, listaExercicios):
    arquivo = open(f"{path}/{categoria}", "w") # removi .txt

    for i in range(len(listaExercicios)):
        arquivo.write(f"{listaExercicios[i].strip()}\n") # precisa do .strip() pra apagar  aquebra de linha '\n' e adicionar de novo
    arquivo.close()

def addExercicio(path, categoria, exercicios, exercicio):
    exercicios.append(exercicio)
    arquivo = open(f"{path}/{categoria}", "w") # removi .txt
    for i in range(len(exercicios)):
        arquivo.write(f"{exercicios[i].strip()}\n") # precisa do .strip() pra apagar  aquebra de linha '\n' e adicionar de novo
    arquivo.close()
    print()
    print(f"[{exercicio}] foi adicionado!")

def abrirExercicios(path, categoria):
    arquivo = open(f"{path}/{categoria}", "r") # removi .txt
    exercicios = arquivo.readlines()
    arquivo.close()

    return exercicios

def listarExercicios(exercicios):
    # título
    if categoria == "cardio.txt":
        print(" > Aeróbicos <")
    elif categoria == "forca.txt":
        print(" > Força <")
    elif categoria == "flexibilidade.txt":
        print(" > Flexibilidade <")
    elif categoria == "equilibrio.txt":
        print(" > Equilíbrio <")
    
    # lisa dos exercícios
    if len(exercicios) > 0:
        for i in range(len(exercicios)):
            print(f"{i+1} | {exercicios[i].strip()}") # print de cada linha do arquivo
    else: 
        print("Sem exercícios cadastrados")



while True:
    opcao = menu()

    if opcao == 1:
        path = path = "files/treinos"
    elif opcao == 2:
        path = path = "files/exercicios"

    # - - - - > TREINOS
    if opcao == 1:
        while True:
            textos = ["Nome: ", "Tipo [categoria]: ", "Duração (em minutos): ", "Objetivo: ", "Observações: "]

            opcaoTreino = menuTreino()
            renomearArquivo(path) # organiza todos os arquivos

            if opcaoTreino == 1: # add
                dicionarioTreino = {}

                print("- Adicionar treino novo -")
                # print("(Digite 0 a qualquer momento para cancelar)\n") # Adicionar isso aqui

                dicionarioTreino = {
                'nome':       input("Nome: "),
                'tipo':       input("Tipo [categoria]: "),
                'duracao':    float(input("Duração (em minutos): ")),
                'objetivo':   input("Objetivo: "),
                'observacao': input("Observações: ")
                }

                treinoTag = ["Nome: ", "Tipo [categoria]: ", "Duração (em minutos): ", "Objetivo: ", "Observações: "]
                salvarArquivo(path, dicionarioTreino, treinoTag) # criar .txt
                print("Treino salvo!")

            elif opcaoTreino == 2: # mostrar
                while True:
                    print("- Ver treinos -")
                    mostrarArquivos(path, "Treino")
                    print(">>> 0 - Sair")
                    opcao = int(input("Qual treino deseja visualizar? "))
                    if opcao <= len((os.listdir(path))) and opcao > 0:
                        mostrarArquivo(path, opcao)
                    elif opcao == 0:
                        break
                    else: 
                        print("Opção inválida.\n")

              
            elif opcaoTreino == 3: # editar
                while True: 
                    print("- Editar treinos - ")
                    mostrarArquivos(path, "Treinos")
                    print("\n0 - Sair")
                    numArquivo = int(input("Selecione o número do arquivo: "))
                    if numArquivo == 0: # ??
                        break
                    editarArquivo(path, numArquivo, textos)

            elif opcaoTreino == 4: # excluir
                print("- Excluir arquivo -")
                mostrarArquivos(path, "Treino")
                numArquivo = int(input("Qual arquivo deseja excluir? "))
                mostrarArquivo(path, numArquivo)
                print(f"Tem certeza que deseja apagar o Treino {numArquivo}")
                print("1 - Sim | 0 - Não")
                delete = int(input("[1/0]: "))
                if delete == 1:
                    apagarArquivo(path, numArquivo)
                    print("O Treino foi deletado.")
                elif delete == 0:
                    print("Cancelado! O arquivo não foi deletado.")
                
                else:
                    print("Opção inválida!")


            elif opcaoTreino == 0:
                break

    # - - - - > EXERCÍCIOS
    elif opcao == 2:
        while True:
            opcaoExercicio = menuExercicio() # MENU

            # OPÇÕES
            if opcaoExercicio == 1: # adicionar exercícios
                while True:
                    print("- Adicionar exercício novo -")
                    categoria = categoriaExercicio()

                    if categoria == 0:
                        break
                    elif categoria == "invalido":
                        print("Tente novamente ou aperte '0 - Voltar'")
                        continue # pula o print, reinicia o loop
                    
                    print() # pular linha

                    exercicio = input("Nome: ").capitalize() # primeira letra maiuscula
                    exercicios = abrirExercicios(path, categoria)
                    addExercicio(path, categoria, exercicios, exercicio)

            elif opcaoExercicio == 2: # listar exercícios
                while True:
                    print("- Ver exercícios -")
                    categoria = categoriaExercicio() # retorna o arquivo: "categoria.txt" 

                    if categoria == 0:
                        break
                    elif categoria == "invalido":
                        print("Tente novamente ou aperte '0 - Voltar'")
                        continue # pula o print, reinicia o loop

                    exercicios = abrirExercicios(path, categoria)
                    listarExercicios(exercicios)

            elif opcaoExercicio == 3: # editar exercícios
                while True:
                    print("- Editar exercícios -")
                    print("Qual a categoria do exercício que você deseja editar?")
                    categoria = categoriaExercicio() # retorna o arquivo: "categoria.txt" 

                    if categoria == 0:
                        break
                    elif categoria == "invalido":
                        print("Tente novamente ou aperte '0 - Voltar'")
                        continue # pula o print, reinicia o loop

                    exercicios = abrirExercicios(path, categoria)
                    print("Qual exercício deseja editar?")
                    listarExercicios(exercicios)
                    print()
                    indice = int(input("Exercício nº: "))-1
                    novoExercicio = input("Novo texto: ").capitalize() # editar
                    print(exercicios[indice])
                    exercicios[indice] = novoExercicio

                    atualizarExercicios(path, categoria, exercicios)
                    
                    

            elif opcaoExercicio == 4: # excluir exercícios
                print("- Excluir exercícios -")

                while True:
                    # print("Qual categoria de exercício você deseja editar?")
                    categoria = categoriaExercicio() # retorna o arquivo: "categoria.txt" 

                    if categoria == 0:
                        break
                    elif categoria == "invalido":
                        print("Tente novamente ou aperte '0 - Voltar'")
                        continue # pula o print, reinicia o loop

                    exercicios = abrirExercicios(path, categoria)
                    # deletar
                    print("Qual exercício deseja deletar?")
                    listarExercicios(exercicios)
                    print()
                    indice = int(input("Exercício nº: "))-1

                    # confirmação
                    while True:
                        print(f"Deseja apagar exercício [{exercicios[indice].strip()}]?")
                        confirmacao = int(input("1 - Sim / 0 - Não: "))

                        if confirmacao == 1: # sim
                            exercicios.pop(indice) # deletar
                            atualizarExercicios(path, categoria, exercicios)
                            print("Exercício deletado!")
                            break
                        elif confirmacao == 0: # não
                            print("Cancelado!")
                            break
                        else:
                            print("Opção inválida!")
                            continue


            elif opcaoExercicio == 0: # fim
                print("break")
                break


