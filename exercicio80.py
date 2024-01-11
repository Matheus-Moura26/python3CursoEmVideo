continuar = 's'
myList = []

while continuar == 's':
    digito = int(input("Digite um número: "))
    
    inserido = False
    for p, v in enumerate(myList):
        if digito < v:
            myList.insert(p, digito)
            inserido = True
            break
        
    if not inserido:
        myList.append(digito)

    continuar = input("Deseja continuar? s / n: ")

print(myList)
