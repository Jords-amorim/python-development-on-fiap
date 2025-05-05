# Sistema que gerencia um cadastro de usuários, baseada em dicionários.

op = 0
ficha = {} #criação do dicionário vazio
while op != 4:
    print("\nFICHA CADASTRAL")
    print("1 - Incluir informações na ficha")
    print("2 - Recuperar informação da ficha")
    print("3 - Exibir a ficha completa ")
    print("4 - Sair")
    op = int(input("Informe a opção desejada: "))
    if op == 1:
        chave = input("\nEm qual campo deseja inserir dados? ")
        if chave in ficha.keys():
            print(f"{chave} -> {ficha.get(chave)}")
            update_chave = input("Você deseja alterar o valor? (S/N)")
            if update_chave == "S":
                valor = input(f"Qual é o novo valor para o campo {chave}? ")
                ficha.update({chave:valor})
            else: 
                valor = input(f"Qual é o dado que deseja incluir no campo {chave}? ")
                ficha.update({chave:valor})
    elif op == 2:
        print(f"\nOs campos disponíveis na ficha são: {ficha.keys()}")
        chave = input("Você deseja obter dados de qual campo? ")
        if chave in ficha.keys():
            print(f"{chave} -> {ficha.get(chave)}")
        else:
            print("O campo informado não existe na ficha cadastral.")
    elif op == 3:
        print("\n---FICHA---")
        for campo, dado in ficha.items():
            print(f"{campo.upper()} -> {dado}")
        print("---------------------------")
    elif op == 4:
        print("Saindo do sistema de ficha cadastral")
        break
    else:
        print("Por favor, escolha uma opção válida")