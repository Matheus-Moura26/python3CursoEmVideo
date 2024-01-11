my_list = []

for count in range(5):
    digito = int(input("Digite um valor numérico: "))
    
    if digito in my_list:
        print("Este valor já existe na lista")
    else:
        my_list.append(digito)

my_list.sort()
print(f"A lista ficou com os números: {my_list}")
