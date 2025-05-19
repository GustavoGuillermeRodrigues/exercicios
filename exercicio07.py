import json
import os

# clientes = []

db_clientes = "db_clientes.json"
def carregar_dados():
    if os.path.exists(db_clientes):
        with open(db_clientes, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []

def obter_dados_dos_clientes():
    nome_cliente = input("Digite seu nome completo: ")
    CPF_cliente = int(input("Digite seu CPF: "))
    RG_cliente = int(input("Digite seu RG: "))
    nascimento_cliente = input("Digite sua data de nascimento (Use '/' para separar os numeros. EX: 1/1/1111: ")
    endereco_cliente = input("Digite seu endereço: ")
    cidade_cliente = input("Digite sua Cidade: ")
    estado_cliente = input("Digite seu Estado: ")
    telefone_cliente = int(input("Digite seu telefone: "))
    celular_cliente = int(input("Digite seu celular: "))
    email_cliente = input("Digite seu email: ")

    cliente = {
        "nome_cliente": nome_cliente,
        "CPF_cliente": CPF_cliente,
        "RG_cliente": RG_cliente,
        "nascimento_cliente": nascimento_cliente,
        "endereco_cliente": endereco_cliente,
        "cidade_cliente": cidade_cliente,
        "estado_cliente": estado_cliente,
        "telefone_cliente": telefone_cliente,
        "celular_cliente": celular_cliente,
        "email_cliente": email_cliente,

    }

    return cliente

def cadastrar_cliente(dados_cliente):
    clientes = carregar_dados()
    clientes.append(dados_cliente)

    with open(db_clientes, "w", encoding="utf-8") as arq_json:
        json.dump(clientes, arq_json, indent=4, ensure_ascii=False)



def mostrar_dados_cliente(dados_clientes):
    for cliente in dados_clientes:
        print(f"""
              Nome do cliente: {cliente["nome_cliente"]})
              CPF do cliente: {cliente["DPF_cliente"]})
              RG do cliente: {cliente["RG_cliente"]})
              Nascimento do cliente: {cliente["nascimento_cliente"]})
              Endereço do cliente: {cliente["endereco_cliente"]})
              Cidade do cliente: {cliente["cidade_cliente"]})
              Estado do cliente: {cliente["estado_cliente"]})
              Telefone do cliente: {cliente["telefone_cliente"]})
              Celular do cliente: {cliente["celular_cliente"]})
              Email do cliente: {cliente["email_cliente"]}
""")

def iniciar_sistema():
    clientes = carregar_dados()
    while True:
        print("")
        print("="*80)
        print("Opçao 1 - Mostrar lista de clientes")
        print("Opçao 2 - Cadastrar clientes")
        print("Opçao 3 - Sair do sistema")
        print("="*80)

        opicao = input("Escolha uma das opçções do Menu: ")

        if opicao == "1":
            mostrar_dados_cliente(clientes)
        elif opicao == "2":
            cadastrar_cliente(obter_dados_dos_clientes())
        elif opicao == "3":
            print("Sistema finalizado!")
        else:
            print("Opção invalida, escolha uma opição no Menu.")

iniciar_sistema()