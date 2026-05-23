# Jogo simples de adivinhar o número aleatório

import random

menor_numero = 1
maior_numero = 50
resposta = random.randint(menor_numero, maior_numero)
tentativas = 0
jogando = True

print("Jogo de adivinhar o número!")
print(f"Tente adivinhar o número que está entre {menor_numero} e {maior_numero}!")

while jogando:
    chute = (input("Adivinhe: "))

    if chute.isdigit():
        chute = int(chute)
        tentativas += 1

        if chute < menor_numero or chute > maior_numero:
            print("Uh, acho que foi longe demais, não?")
            print(f"Por favor, tente outro número entre {menor_numero} e {maior_numero}!")
        elif chute < resposta:
            print("Uff, baixo! Tente de novo!")
        elif chute > resposta:
            print("Uff, alto! Tente de novo!")
        else:
            print(f"CORRETO! A resposta era {resposta}")
            print(f"Número de tentativas: {tentativas}")
            jogando = False
    else:
        print("Inválido.")
        print(f"Por favor, tente outro número entre {menor_numero} e {maior_numero}!")
