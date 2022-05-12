import random


def play():
    print(25*"/")
    print("/   O Jogo da Forca     / ")
    print(25*"/","\n")




    pais_secreto = [('brasil'), ('australia'), ('japao'), ('canada'), ('gana'), ('grecia'),('peru'), ('china'), ('chile'), ('cuba'), ('belgica'), ('polonia'), ('jamaica'), ('paraguai'), ('alemanha'), ('zimbabue'), ('argentina'), ('dinamarca'), ('madagascar'), ('eslovaquia'), ('montenegro')]
    random.shuffle(pais_secreto)
    pais_secreto = (pais_secreto[0])
    enforcou = False
    escapou = False

    print("Jogando o Jogo da Forca" "\n")

    while(not enforcou and not escapou):
        print(f"O pais tem {pais_secreto.__len__()} letras? _ _ _ _ _ _")
        chute = input("chute uma letra: ")
        posicao = 0
        if (chute in pais_secreto):
            print(f"O país tem a letra {chute}, na posição {posicao}")
        else:
            print(f"não tem a letra {chute}, no pais!")
            posicao = posicao + 1

    print("Fim de jogo")

if(__name__ == "__main__"):
    play()


