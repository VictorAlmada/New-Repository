import os

x = True
while x:
    n1 = int(input("Primeiro n°: "))
    os.system("cls")
    while True:
        operador = input(f"{n1}  \nOperador: ")
        os.system("cls")
        if operador == "+":
            break
        elif operador == "-":
            break
        elif operador == "*":
            break
        elif operador == "/":
            break
        else:
            print("Operador inválido!")
    n2 = int(input(f"{n1} {operador} \nSegundo n°: "))
    os.system("cls")
    if operador == "+":
        result = n1+n2
    elif operador == "-":
        result = n1-n2
    elif operador == "*":
        result = n1*n2
    else:
        result = n1/n2
    print(f"{n1} {operador} {n2} = {result}")
    while True:
        novo = str(input("Novo cálculo? "))
        os.system("cls")
        if novo == "n":
            x = False
            break
        elif novo == "s":
            x = True
            break
