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

    
print(f"""

A: {len(myList)} números foram digitados e inclusos na lista
B: {sorted(myList, reverse=True)}
C: {"5 foi digitado e está na lista" if 5 in myList else "5 não está na lista"}

""")
