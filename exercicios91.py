import time
import random

dados = {
    "jogador1": 0,
    "jogador2": 0,
    "jogador3": 0,
    "jogador4": 0
}

for jogador, valor in dados.items():
    val = random.randint(0, 6)
    print(f"O jogador {jogador} jogou o valor {val}")
    dados[jogador] = val
    time.sleep(0.3)

print("Dados:", dados)

posicionamento = {
    "1° primeiro": 0,
    "2° segundo": 0,
    "3° terceiro": 0,
    "4° quarto": 0,
}

# Atualiza os valores de posicionamento com base nos valores de dados
for count, (key, value) in enumerate(dados.items()):
    if count < 4:
        posicionamento[list(posicionamento.keys())[count]] = value

for key, value in posicionamento.items():
    count = 0
    for k, v in dados.items():
        if value - v <= 0:
            count += 1
            posicionamento[key] = v


print("Posicionamento:", posicionamento)
