listaTotal = []
listaPar= []
ListaImpar= []

for c in range(1,10):
    listaTotal.append(c)
    if c%2 ==0:
        listaPar.append(c)
    else:
        ListaImpar.append(c)

outralistapar= []
outralistaimpar = []

for c in range(1, len(listaTotal)):
    if c%2 ==0:
        outralistapar.append(c)
    else:
        outralistaimpar.append(c)


print(f"""

    A lista com todos os itens é {listaTotal}
    A lista com os itens pares é {outralistapar}
    A lista com os itens impares é {outralistaimpar}
""")