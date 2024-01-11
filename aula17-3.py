#Desafio 078

lista = []
maior = 0
menor = 500
for count in range(0,5):
    numero = int(input("Digite um valor numérico"))
    lista.append(numero)
    if numero > maior:
        maior = numero
        if numero < menor:
           menor = numero
    elif numero < menor:
        menor = numero

print(f"""
      
    O maior valor digitado foi {maior}
    O menor valor digitado foi {menor}
    A lista é {lista}
""")

