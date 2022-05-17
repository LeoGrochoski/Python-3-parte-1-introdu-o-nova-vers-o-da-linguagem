import random

def play():
    print(25*"/")
    print("/   O Jogo da Forca     / ")
    print(25*"/","\n")

    pais_secreto = ['brasil', 'australia', 'japao', 'canada', 'gana', 'grecia','peru', 'china', 'chile', 'cuba', 'belgica', 'polonia', 'jamaica', 'paraguai', 'alemanha', 'zimbabue', 'argentina', 'dinamarca', 'madagascar', 'eslovaquia', 'montenegro']
    random.shuffle(pais_secreto)
    pais_secreto = (pais_secreto[0])
    letras_acertadas = ("_" * len(pais_secreto))
    letras_certas = (list(letras_acertadas))

    enforcou = False
    escapou = False

    while(not enforcou and not escapou):
        print(f"O país tem {len(pais_secreto)} letras.", "\n")

        chute = input("chute uma letra: ")
        chute = chute.strip()

        posicao = 0
        for letra in pais_secreto:
            if (chute.upper() == letra.upper()):
                letras_certas[posicao] = letra
            posicao = posicao + 1

        print(letras_certas)

if(__name__ == "__main__"):
    play()


