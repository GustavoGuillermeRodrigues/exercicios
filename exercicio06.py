def cadastrar_filme(nome_filme, descricao, classificacao, categoria01, categoria02, categoria03):
    filmes = []
    filme = {
        "nome_filme": nome_filme,
        "descricao": descricao,
        "classificacao": classificacao,
        "categorias": [categoria01, categoria02, categoria03]

    }

    filmes.append(filme)
    return filmes
print(cadastrar_filme("minecraft", "é uma comédia de aventura de 2025 que se passa no universo do videogame Minecraft", 10, "aventura", "comedia", "animacao"))