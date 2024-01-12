dados = dict()
lista = list()
for count in range(0,1):
    dados["nome"] = input("Nome do aluno: ")
    dados["media"] = int(input("Digite a media do aluno: "))
    if dados["media"] >= 6:
        status = "Passou"
    else:
        status = "Reprovou"
    dados["status"] = status
    lista.append(dados.copy())

for aluno in lista:
    for key, value in aluno.items():
        if key == "nome":
            print(f"Nome do aluno é: {value}")
        elif key == "media":
            print(f"Media do aluno é: {value}")
        else:
            print(f"Status do aluno: {value}")
