"""Problema 5: Estoque de Produtos
Desenvolva um sistema de controle de estoque de produtos. Crie um dicionário
onde as chaves são os nomes dos produtos e os valores são as quantidades 
disponíveis em estoque. Permita que o usuário faça pedidos de produtos
e atualize o estoque conforme necessário."""

v = "s"
t = ""
dicionario = dict()

while v == "s":
    t = input("""Pressione 1 se deseja adicionar ao estoque
ou presssione 2 se deseja fazer um pedido reduzindo estoque""")
    if t == "1":
        nome = input("Qual o nome do produto que você deseja adicionar?")
        quantidade = int(input("Qual a quantidade do produto que você deseja adicionar?"))
        if nome in dicionario:
            dicionario[nome] += quantidade
            print(f"""Foi adicionado {quantidade} unidades ao produto {nome}""")
        else:
            dicionario[nome] = quantidade
            print(f"""Foi adicionado o produto: {nome} com {quantidade} unidades""")
    elif t == "2":
        nome = input("Qual o nome do produto que você deseja comprar?")
        quantidade = int(input("Qual a quantidade do produto que você deseja comprar?"))
        if dicionario[nome] - quantidade >= 0 and nome in dicionario:
            dicionario[nome] -= quantidade
            print(f""" Parabens!! Você comprou {quantidade} unidades do produto
                  {nome} se desejar mais ainda tempos {dicionario[nome]-quantidade} unidades no estoque
                  Além do mais possuímos os seguintes produtos no estoque: 
                  {dicionario}""")
        else:
            print(f"Temos apenas {dicionario[nome].value()} unidades deste produto, você digitou {quantidade}")
            
    v = input("Deseja fazer uma venda ou adicionar produtos ao estoque novamente? s/n: ")