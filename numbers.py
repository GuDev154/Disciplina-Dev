import random

a = random.randint(1,30)
b = random.randint(30, 60)
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

def menu():
    print("-- Menu de operações --")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    