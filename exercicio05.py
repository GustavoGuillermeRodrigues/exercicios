from exercicio04 import somar_notas

alunos = []

def obter_dados():
    nome_aluno = input("Informe o nome completo do aluno: ")
    email_aluno = input("Informe o email do aluno: ")
    serie_aluno = input("Informe a serie do aluno: ")
    nota01 = float(input("Digite a nota01 do aluno: "))
    nota02 = float(input("Digite a nota02 do aluno: "))
    nota03 = float(input("Digite a nota03 do aluno: "))

    return cadastrar_aluno(nome_aluno, email_aluno, serie_aluno, nota01, nota02, nota03)

def cadastrar_aluno(nome, email, serie, nota01=0, nota02=0, nota03=0):

    notas = [nota01, nota02, nota03]

    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie,
        "nota": notas,
        "media": somar_notas(notas)
    }

    alunos.append(aluno)
    media = somar_notas(aluno["nota"])

    return alunos

def mostrar_dados(dados_alunos):
    for aluno in dados_alunos:
        print(f"Nome Do Aluno: {aluno["nome"]} | Email do Aluno: {aluno["email"]} | Serie do Aluno: {aluno["serie"]} | Notas do aluno: {aluno["notas"]} | Media do Aluno: {aluno["media"]}")
        
    return print(dados_alunos)

def iniciar_sistema():
    while True:
        print("="*80)
        print("Opção 1 => Mostrar lista de alunos cadastrados.")
        print("Opção 2 => Cadastrar Alunos.")
        print("Opção 3 => Sair do sistema.")
        print("="*80)

        opcao = input("Escolha uma das opções a cima: ")

        if opcao == "1":
            mostrar_dados(alunos)
        elif opcao == "2":
            obter_dados()
        else:
            print("Sistema finalizado")
            break
            

iniciar_sistema()