# Segunda tentativa de fazer uma calculadora em Python, dessa vez uma mais simples.

print("Operações disponiveis: +, -, *, /")
numero1 = float(input("Digite o primeiro número: "))
operacao = input("Selecione a operação: ")
numero2 = float(input("Digite o segundo número: "))

if operacao == "+":
    print(f"Resultado:", (numero1 + numero2))
elif operacao == "-":
    print(f"Resultado:", (numero1 - numero2))
elif operacao == "*":
    print(f"Resultado:", (numero1 * numero2))
elif operacao == "/":
    if numero2 == 0:
        print("Ei... Sem tentar dividir por 0.")
    else:
        print(f"Resultado:", (numero1 / numero2))
else:
    print("Operação inválida.")
