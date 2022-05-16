import random


def play():
    print(25*"/")
    print("/   O Jogo da Forca     / ")
    print(25*"/","\n")

    pais_secreto = ['brasil', 'australia', 'japao', 'canada', 'gana', 'grecia','peru', 'china', 'chile', 'cuba', 'belgica', 'polonia', 'jamaica', 'paraguai', 'alemanha', 'zimbabue', 'argentina', 'dinamarca', 'madagascar', 'eslovaquia', 'montenegro']
    random.shuffle(pais_secreto)
    pais_secreto = (pais_secreto[0])
    tamanho_pais = ""
    enforcou = False
    escapou = False
    print(pais_secreto)

    print("Jogando o Jogo da Forca" "\n")

    while(not enforcou and not escapou):
        print(f"O país tem {pais_secreto.__len__()} letras.")
        if (pais_secreto.__len__() == 4):
            tamanho_pais = "_ _ _ _"
            print(tamanho_pais)
        elif(pais_secreto.__len__() == 5):
            tamanho_pais = "_ _ _ _ _"
            print(tamanho_pais)
        elif(pais_secreto.__len__() == 6):
            tamanho_pais = "_ _ _ _ _ _"
            print(tamanho_pais)
        elif (pais_secreto.__len__() == 7):
            tamanho_pais = "_ _ _ _ _ _ _"
            print(tamanho_pais)
        elif (pais_secreto.__len__() == 8):
            tamanho_pais = "_ _ _ _ _ _ _ _"
            print(tamanho_pais)
        elif (pais_secreto.__len__() == 9):
            tamanho_pais = "_ _ _ _ _ _ _ _ _"
            print(tamanho_pais)
        elif (pais_secreto.__len__() == 10):
            tamanho_pais = "_ _ _ _ _ _ _ _ _ _"
            print(tamanho_pais)

        chute = input("chute uma letra: ").casefold()
        chute = chute.strip()

        posicao = 0
        for letra in pais_secreto:
            if (chute == letra):
                print(f"O país tem a letra {chute}, na posição {posicao}")
            posicao = posicao + 1
        print("Jogando...")


if(__name__ == "__main__"):
    play()


