# Jogo simples de pedra, papel ou tesoura.

import random

opcoes = ("pedra", "papel", "tesoura")
jogando = True

while jogando:
    jogador = None
    computador = random.choice(opcoes)

    while jogador not in opcoes:
        jogador = input("Selecione pedra, papel ou tesoura: ").lower()

    print(f"Jogador: {jogador}")
    print(f"Computador: {computador}")

    if jogador == computador:
        print("Empate!")
    elif jogador == "pedra" and computador == "tesoura":
        print("Você ganhou!")
    elif jogador == "papel" and computador == "pedra":
        print("Você ganhou!")
    elif jogador == "tesoura" and computador == "papel":
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    if not input("Jogar novamente? (Y/N): ").lower() == "y":
        jogando = False
