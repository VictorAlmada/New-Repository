
nome = ""
senha = ""
cadastro = False


def logout():
    print("Sessão encerrada!")
    intro()


def sistema():
    print(f"Oque deseja fazer {nome.title()}:")
    print("1. Mudar senha")
    print("2. Logout")
    escolha = input("Digite a opção desejada: ")
    if escolha == "1":
        mudar_senha()
    elif escolha == "2":
        logout()
    else:
        print("Opção inválida!")
        sistema()


def mudar_senha():
    global senha
    mudar_a_senha = input("Digite a senha atual: ")
    if mudar_a_senha == senha:
        senha = input("Digite a nova senha: ")
        print("### Senha atualizada! ###")
        sistema()
    else:
        print("### Senha incorreta! ###")
        sistema()


def intro():
    global cadastro
    print("-----Bem-vindo ao sistema!-----")
    print("Oque deseja fazer?")
    print("1. Cadastrar Usuário")
    print("2. Login")
    print("3. Sair do sistema")
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        if not cadastro:
            print("### Não há cadastro! ###")
            intro()
        else:
            login()
    elif opcao == "3":
        print("### Finalizando o sistema! ###")
        return 0
    else:
        print("### Opção inválida! ###")
        intro()


def cadastrar():
    global nome
    global senha
    global cadastro
    if nome != "":
        print("### Usuário já cadastrado! ###")
        novo_cadastro = input("Realizar novo cadastro? (s/n): ")
        if novo_cadastro == "s":
            nome = ""
            cadastrar()
        else:
            intro()
    else:
        print("-----Cadastro-----")
        nome = input("Nome de usuário: ")
        senha = input("Senha: ")
        print("### Usuário cadastrado com sucesso! ###")
        cadastro = True
        intro()


def login():
    global nome
    global senha
    print("-----Login-----")
    login_nome = input("Nome de usuário: ")
    login_senha = input("Senha: ")
    if login_nome == nome and login_senha == senha:
        print("### Acesso autorizado! ###")
        print(f"### Seja bem-vindo {nome.title()}! ###")
        sistema()
    else:
        print("### Nome de usuário ou senha inválidos! ###")
        intro()


intro()
