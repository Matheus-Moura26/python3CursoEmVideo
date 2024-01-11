n = 0

expressao = input("Digite uma expressao! ")
for c in expressao:
    if c == "(":
        n+=1
    elif c == ")":
        n-=1
    else:
        pass
if n == 0:
    print("Esta expressão é valida")
else:
    print("Esta expressão não é valida")
