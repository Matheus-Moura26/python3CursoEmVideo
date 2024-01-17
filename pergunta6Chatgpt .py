usuarios = dict()

while True:
    print("Deseja criar novo usuário ou fazer login?")
    opcao = int(input("1 para criar usuário e 2 para login: "))

    if opcao == 1:
        nome = input("Qual seu nome? ")
        usuarios[nome] = dict()
        usuarios[nome]["email"] = input("Qual seu email? ")
        usuarios[nome]["idade"] = input("Qual sua idade? ")
        usuarios[nome]["senha"] = input("Digite uma senha: ")
        print(f"Usuário {nome} cadastrado com sucesso!")

    elif opcao == 2:
        nome = input("Qual seu nome? ")
        senha = input("Qual sua senha? ")

        if nome in usuarios and usuarios[nome]["senha"] == senha:
            print("Parabéns, você fez login com sucesso!")
        else:
            print("Erro: Nome de usuário ou senha incorretos.")

    continuar = input("Se deseja cadastrar ou fazer login novamente, digite 's'. Para finalizar, digite 'n': ")
    if continuar.lower() == 'n':
        break
