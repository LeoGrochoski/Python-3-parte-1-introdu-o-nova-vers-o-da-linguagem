import random


def play():
    print(25*"/")
    print("/   O Jogo da Forca     / ")
    print(25*"/","\n")

    secret_country = "brasil"
    hanged = False
    escaped = False

    secret_country = [('brasil'), ('australia'), ('japao'), ('canada'), ('gana'), ('grecia'),('peru'), ('china'), ('chile'), ('cuba'), ('belgica'), ('polonia'), ('jamaica'), ('paraguai'), ('alemanha'), ('zimbabue'), ('argentina'), ('dinamarca'), ('madagascar'), ('eslovaquia'), ('montenegro')]
    random.shuffle(secret_country)
    secret_country = (secret_country[0])


    while(not hanged and not escaped):
        print("Jogando o Jogo da Forca" "\n")
        print(f"O pais tem {secret_country.__len__()} letras? _ _ _ _ _ _")
        shot = input("chute o pais: ")
        if(shot in secret_country):
            print(f"O pais tem a letra {shot}")
            break
        else:
            print(f"o pais não é {shot}!")

    print("Fim de jogo")

if(__name__ == "__main__"):
    play()


