clientes = []
cliente_logado = None


def cadastro():
    nome = input("Digite seu nome:")
    email = input("Digite seu e-mail:")
    senha = input("Digite sua senha:")
    confirmaSenha = input("Confirme sua senha:")

    if senha != confirmaSenha:
        print("As senhas não coincidem")
        return

    cliente = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "plano": None
    }

    clientes.append(cliente)
    print("--------------cadastro realizado com sucesso-----------------")
    print("")


def login():
    email = input("Digite seu e-mail:")
    senha = input("Digite sua senha:")

    for cliente in clientes:
        if cliente["email"] == email and cliente["senha"] == senha:
            print("---------------Login realizado com sucesso !!!------------")
            print("")
            return cliente

    print("Email ou senha incorretos")
    return None


planos = [
    {
        "nome": "beta",
        "preco": 10.0,
        "beneficios": ["beneficio 1", "beneficio 2"]
    },
    {
        "nome": "premium",
        "preco": 20.0,
        "beneficios": ["beneficio 1", "beneficio 2", "beneficio 3"]
    },
    {
        "nome": "master",
        "preco": 30.0,
        "beneficios": ["beneficio 1", "beneficio 2", "beneficio 3", "beneficio 4"]
    }
]


def escolher_plano(cliente):
    print("Escolha seu plano de assinatura")
    for i, plano in enumerate(planos):
        print(f"{i+1}. {plano['nome']} - R${plano['preco']}")

    opcao = int(input("Digite a opção do plano desejado:"))
    if opcao < 1 or opcao > len(planos):
        print("Opção inválida")
        return

    plano_escolhido = planos[opcao - 1]
    cliente["plano"] = plano_escolhido
    return plano_escolhido


def exibir_detalhes_cliente(cliente):
    print("Detalhes do cliente:")
    print(f"Nome: {cliente['nome']}")
    print(f"E-mail: {cliente['email']}")
    if cliente["plano"]:
        print("Plano de Assinatura:")
        print(f"Nome: {cliente['plano']['nome']}")
        print(f"Preço: R${cliente['plano']['preco']}")
        print("Benefícios:")
        for beneficio in cliente["plano"]["beneficios"]:
            print(f"- {beneficio}")
    else:
        print("O cliente não escolheu um plano de assinatura")


# Exemplo de uso do sistema
while True:
    print("===== Sistema de Assinatura =====")
    print("1. Cadastrar cliente")
    print("2. Fazer login")
    print("3. Escolher plano de assinatura")
    print("4. Exibir detalhes do cliente")
    print("5. Sair")

    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 1:
        cadastro()
    elif opcao == 2:
        cliente_logado = login()
        if cliente_logado is None:
            continue
    elif opcao == 3:
        if cliente_logado:
            escolher_plano(cliente_logado)
        else:
            print("Faça login primeiro")
            print("")
    elif opcao == 4:
        if cliente_logado:
            exibir_detalhes_cliente(cliente_logado)
        else:
            print("Faça login primeiro")
            print("")
    elif opcao == 5:
        break
    else:
        print("Opção inválida")

print("Sistema encerrado.")
