"""Problema 4: Jogo de Dados
Crie um jogo simples onde os jogadores lançam dados. Registre os resultados
dos jogadores em um dicionário, onde as chaves são os nomes dos jogadores e os
valores são as somas dos valores dos dados."""
import random

v = "s"
dicionario = dict()

while v =="s":
    nome = input("Qual o nome do jogador? ")
    v = input("Deseja jogar dado? s/n: ")
    if v == "s":
        dado = random.randint(0,6)
        print(f"Recebeu o valor {dado}")
    else:
        break
    dicionario[nome] = dado
    v = input("Há outro jogador para jogar? s/n: ")

print(f"""Os seguintes jogadores obtiveram os seguintes valores:
       {dicionario}""")