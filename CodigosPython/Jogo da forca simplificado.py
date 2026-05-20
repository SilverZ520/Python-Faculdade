import random


def iniciar_jogo():
    # Lista usada para armazenar as palavras disponíveis para o sorteio.
    lista_palavras = ["PYTHON", "PROGRAMACAO", "ESTRUTURA", "ALGORITMO", "COMPUTADOR"]

    palavra_secreta = random.choice(lista_palavras)
    palavra_oculta = ["_"] * len(palavra_secreta)
    letras_tentadas = set()
    tentativas_restantes = 6

    return palavra_secreta, palavra_oculta, letras_tentadas, tentativas_restantes


def processar_tentativa(letra, palavra_secreta, palavra_oculta, letras_tentadas):
    # O conjunto evita que a mesma letra seja registrada mais de uma vez.
    letras_tentadas.add(letra)

    if letra in palavra_secreta:
        for indice, caractere in enumerate(palavra_secreta):
            if caractere == letra:
                palavra_oculta[indice] = letra

        print("Boa! A letra existe na palavra.")
        return True

    print("A letra digitada não faz parte da palavra.")
    return False


palavra_secreta, palavra_oculta, letras_tentadas, tentativas_restantes = iniciar_jogo()

print("Bem-vindo ao jogo da forca!")

while tentativas_restantes > 0 and "_" in palavra_oculta:
    print("\nPalavra:", " ".join(palavra_oculta))
    print("Tentativas restantes:", tentativas_restantes)

    if letras_tentadas:
        print("Letras já tentadas:", ", ".join(sorted(letras_tentadas)))

    letra = input("Digite uma letra: ").upper().strip()

    # Validação para garantir que o usuário digite apenas uma letra.
    if len(letra) != 1 or not letra.isalpha():
        print("Digite apenas uma letra válida.")
        continue

    if letra in letras_tentadas:
        print("Você já tentou essa letra anteriormente.")
        continue

    acertou = processar_tentativa(
        letra,
        palavra_secreta,
        palavra_oculta,
        letras_tentadas
    )

    if not acertou:
        tentativas_restantes -= 1

if "_" not in palavra_oculta:
    print("\nParabéns! Você descobriu a palavra:", palavra_secreta)
else:
    print("\nFim de jogo! Você ficou sem tentativas.")
    print("A palavra secreta era:", palavra_secreta)

print("Obrigado por jogar!")
