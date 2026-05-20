# Código simples para calcular raiz quadrada.

import math

while True:
    try:
        numero = float(input("Digite um número: "))
        break
    except ValueError:
        print("Por favor, insira apenas um número válido.")

raiz_quadrada = math.sqrt(numero)

print(f"A raiz quadrada de {numero} é {raiz_quadrada}")
