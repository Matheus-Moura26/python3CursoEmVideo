"""Ranking de Palavras:
Escreva um programa que conte a frequência de cada palavra em um texto longo.
Use um dicionário para armazenar as palavras e suas contagens. Exclua 
palavras comuns (artigos, preposições) da contagem."""

texto = input("Escreva um texto").lower()

texto1 = texto.split(" ")
dicionario = dict()
vogais = ["a","e","i","o","u"]
for palavra in texto1:
    if palavra in dicionario:
        dicionario[palavra] +=1
    else:
        dicionario[palavra] = 1
    if palavra in vogais:
        dicionario.pop(palavra)

print(dicionario)