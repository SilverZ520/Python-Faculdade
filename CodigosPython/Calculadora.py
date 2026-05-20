# Primeira tentativa de fazer uma calculadora em Python.

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Ei... Sem tentar dividir por 0."
    return a / b

print("Operações disponiveis: +, -, *, /")
numero1 = float(input("Digite o primeiro número: "))
operacao = input("Selecione a operação: ")
numero2 = float(input("Digite o segundo número: "))

if operacao == "+":
    print(f"Resultado:", somar(numero1, numero2))
elif operacao == "-":
    print(f"Resultado:", subtrair(numero1, numero2))
elif operacao == "*":
    print(f"Resultado:", multiplicar(numero1, numero2))
elif operacao == "/":
    print(f"Resultado:", dividir(numero1, numero2))
else:
    print("Operação inválida.")
