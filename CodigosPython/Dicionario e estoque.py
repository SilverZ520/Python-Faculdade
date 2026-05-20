# Utilização de um dicionário para facilitar o acesso e a atualização dos produtos pelo nome.

estoque_produtos = {
    "Arroz": {
        "quantidade": 20,
        "preco": 25.90
    },
    "Feijao": {
        "quantidade": 15,
        "preco": 8.50
    },
    "Macarrao": {
        "quantidade": 10,
        "preco": 6.75
    }
}

while True:
    print("\n===== MENU DO SISTEMA =====")
    print("1 - Visualizar Estoque Atual")
    print("2 - Registrar Entrada de Produto")
    print("3 - Registrar Saída de Produto")
    print("4 - Sair do Sistema")

    opcao_usuario = input("Escolha uma opção: ")

    if opcao_usuario == "1":
        print("\n===== ESTOQUE ATUAL =====")

        for produto, dados in estoque_produtos.items():
            print(f"Produto: {produto}")
            print(f"Quantidade: {dados['quantidade']}")
            print(f"Preço: R$ {dados['preco']:.2f}")
            print("-------------------------")

    elif opcao_usuario == "2":
        nome_produto = input("Digite o nome do produto: ")

        # Conversão explícita de string para inteiro utilizando int()
        quantidade_entrada = int(input("Digite a quantidade de entrada: "))

        if nome_produto in estoque_produtos:
            estoque_produtos[nome_produto]["quantidade"] += quantidade_entrada
            print("Quantidade atualizada com sucesso.")
        else:
            print("Produto não encontrado.")

    elif opcao_usuario == "3":
        nome_produto = input("Digite o nome do produto: ")

        # Conversão explícita de string para inteiro utilizando int()
        quantidade_saida = int(input("Digite a quantidade de saída: "))

        if nome_produto in estoque_produtos:

            if estoque_produtos[nome_produto]["quantidade"] >= quantidade_saida:
                estoque_produtos[nome_produto]["quantidade"] -= quantidade_saida
                print("Quantidade atualizada com sucesso.")
            else:
                print("Estoque insuficiente.")

        else:
            print("Produto não encontrado.")

    elif opcao_usuario == "4":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")
