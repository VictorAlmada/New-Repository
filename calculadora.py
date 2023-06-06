def soma(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")


def subt(a, b):
    result = a - b
    print(f"{a} - {b} = {result}")


def mult(a, b):
    result = a * b
    print(f"{a} x {b} = {result}")


def divi(a, b):
    result = a / b
    print(f"{a} / {b} = {result}")


x = True
while x:
    n1 = int(input("Primeiro n°: "))
    n2 = int(input("Segundo n°: "))
    while True:
        operador = input("Operador: ")
        if operador == "+":
            soma(n1, n2)
            break
        elif operador == "-":
            subt(n1, n2)
            break
        elif operador == "*":
            mult(n1, n2)
            break
        elif operador == "/":
            divi(n1, n2)
            break
        else:
            print("Operador inválido!")
    while True:
        novo = input("Novo cálculo? ")
        if novo == "n":
            x = False
            break
        elif novo == "s":
            x = True
            break
        else:
            print("Digite apenas s ou n !")
