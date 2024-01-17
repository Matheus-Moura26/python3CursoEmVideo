#Rascunho
""" 
num = [2,5,9,1]
num[2] =3
num.append(7)
num.sort(reverse=True)
num.insert(2,0)
num.remove(2)
if 4 in num:
    num.remove(4)
else:
    print("4 não está na lista")
print(num)
print(f"Essa lista tem {len(num)} elementos") """





#NOVO RASCUNHO
""" num = 1
valores = []

for count in range(0,4):
    valores.append(num)
    num+=1

valores.sort(reverse=True)

for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}")
print("Chegamos ao final da lista")
print(f"O maior valor é {valores[0]} e o menor valor é {valores[len(valores)-1]}") """



#NOVO RASCUNHO

""" dados = { 'nome': 'Pedro','idade':25}

for k,v in dados.items():
    print(f"O {k} é {v}") """


#NOVO RASCUNHO

""" meuDicionario = {"Chave1": "Valor1","Chave2": "Valor2","Chave3": "Valor3","Chave4": "Valor4",}
print(meuDicionario.get("Chave5" , "Não existe")) """

#NOVO RASCUNHO
""" 
meuDicionario = {"Chave1": "Valor1","Chave2": "Valor2","Chave3": "Valor3","Chave4": "Valor4",}
meuDicionario.setdefault("Chave5" , "KaKaKaKaKaKa")
print(meuDicionario)
 """

#NOVO RASCUNHO

""" meuDicionario = {"Chave1": "Valor1","Chave2": "Valor2","Chave3": "Valor3","Chave4": "Valor4",}
meuDicionario.pop("Chave1", "ValorPadrão")
print(meuDicionario) """


#NOVO RASCUNHO
""" 
dicionario1 = {"a":1,"b":2,"c":3,}
dicionario2 = {"d":4,"e":5,"f":6,}

dicionario1.update(dicionario2)

print(dicionario1)
print(dicionario2)
 """


#NOVO RASCUNHO
""" 
dicionario1 = {"a":1,"b":2,"c":3,}
dicionario2 = {"d":4,"e":5,"f":6,}

dicionario1.update(dicionario2)

print(dicionario1)
print(dicionario2)
"""


#NOVO RASCUNHO

""" 
quadrado = {x: x**2 for x in range(1,100)}
print(quadrado)
 """

