def cadastrar_aluno(nome, email, serie):
    alunos = []
    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie,
    }

    alunos.append(aluno)
    return alunos
print(cadastrar_aluno ("gustavo", "gus@gmail.com", "2B"))

