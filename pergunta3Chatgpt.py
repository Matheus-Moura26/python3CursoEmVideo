"""Problema 3: Sistema de Autenticação Simples
Implemente um sistema de autenticação simples onde os usuários podem se
registrar e fazer login. Utilize um dicionário para armazenar os dados dos
usuários (nome, senha)."""
v = "s"

dicionario = dict()
while v == "s":
    nome = input("Digite o nome para cadastro")
    senha = input("Digite a senha para cadastro")
    if nome in dicionario:
        print("Nome já existe")
    else:
        dicionario[nome] = senha
        print("Usuario criado com sucesso")
    v = input("Deseja fazer mais cadastros? s/n: ")

t = "s"

while t == "s":
    nome = input("Digite o nome para cadastro")
    senha = input("Digite a senha para cadastro")
    if nome in dicionario and dicionario[nome] == senha :
        print("Logado com sucesso")
        break
    else:
        t = input("Houve um erro, gostaria de tentar novamente? s/n: ")