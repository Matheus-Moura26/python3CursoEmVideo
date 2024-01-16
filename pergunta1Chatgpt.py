""" Problema 1: Calculando a Média das Notas
Crie um programa que solicite ao usuário que insira notas de alunos (utilize um
 dicionário onde as chaves são os nomes dos alunos e os valores são as notas). 
 Em seguida, calcule a média das notas e imprima o resultado. """
c = "s" 
historico = {}

while c == "s":
    name = input("Qual seu nome? ")
    grade = int(input("Qual sua nota? "))
    c = input("Deseja continuar? s / n: ")
    historico[name] = grade

total = 0
for v in historico.values():
    total += v
media = total / len(historico)

print(f"A media das notas é {media}")