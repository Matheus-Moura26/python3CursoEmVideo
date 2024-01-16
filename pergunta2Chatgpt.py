"""Problema 2: Contagem de Palavras
Desenvolva um programa que conte a frequência de cada palavra em uma frase 
fornecida pelo usuário. Utilize um dicionário para armazenar as palavras
e suas contagens."""
#O nome da palavra é a key e o número de repetição da palavra é o value

frase= input("Escreva uma frase: ")

palavras = [palavra.strip('.,!?\'').lower() for palavra in frase.split()]

dicionario = dict()

for palavra in palavras:
    if palavra in dicionario:
        dicionario[palavra]+=1
    else:
        dicionario[palavra] = 1

for palavra, contagem in dicionario.items():
    print(f"{palavra} = {contagem}")