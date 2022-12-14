import os
login= []
senha = []

while True:
    opcao = input("""    
    -----------------
    1 - Criar conta
    -----------------
    2 - Entrar
    -----------------
    3 - Sair
    -----------------
    
    Escolha uma opção acima: """)

    if opcao == "1":
        os.system("clear")
        login_cadastrado = input("Cadastrar login: ")
        login.append(login_cadastrado)

        senha_cadastrada = input("Cadastrar senha: ")
        senha.append(senha_cadastrada)
        os.system("clear")
        print("Usuário cadastrado!")

    elif opcao == "2":
        if len(login) == 0 and len(senha) == 0:
            os.system("clear")
            print("\nNão há usuário cadastrado")
        else:
            os.system("clear")
            if input("Entrar: ") == login_cadastrado:
                if input("Senha: ") == senha_cadastrada:
                    os.system("clear")
                    print("Usuário Logado")
                    break
                else:
                    print("Usuário inválido!")
            else:
                print("Usuário inválido!")
    elif opcao == "3":
        os.system("clear")
        print("Programa encerrado!")
        break
        
    else:
        os.system("clear")
        print("Opção inválida")
