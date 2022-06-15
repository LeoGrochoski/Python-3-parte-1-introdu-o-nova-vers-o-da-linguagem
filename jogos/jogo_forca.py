import random

def jogar():

    # Metodo para apresentação do jogo
    print(25 * "/")
    print("/   O Jogo da Forca     / ")
    print(25 * "/", "\n")


    # Metodo implementado para gerar um pais presenta na lista de forma randomica
    pais_secreto = ['brasil', 'australia', 'japao', 'canada', 'gana', 'grecia', 'peru', 'china', 'chile',
                            'cuba', 'belgica', 'polonia', 'jamaica', 'paraguai', 'alemanha', 'zimbabue', 'argentina',
                            'dinamarca', 'madagascar', 'eslovaquia', 'montenegro']
    random.shuffle(pais_secreto)
    pais_secreto = (pais_secreto[0]).upper()
    letras_acertadas = ("_" * len(pais_secreto))
    print(letras_acertadas)
    letras_certas = (list(letras_acertadas))
    print(letras_certas)

    enforcou = False
    escapou = False
    tentativas = 0
    erros = 0

    print(f"O país tem {len(pais_secreto)} letras.", "\n")
    while(not enforcou and not escapou):

        chute = input("chute uma letra: ")
        chute = chute.strip().upper()

        # Logica de chutes, quando errado sobe uma tentativa, ao acertar não sobe
        if chute not in pais_secreto:
            tentativas += 1
        else:
            posicao = 0
            for letra in pais_secreto:
                if(chute == letra):
                    letras_certas[posicao] = letra
                posicao += 1

        # Metodo para quantidade de tentativas ser do tamanho do desenha do corpo humano
        enforcou = tentativas > 6
        if(enforcou == True):
            print("Que pena!")
        print(letras_certas)

        # Metodo para transformar a lista em uma string e finalizar o jogo quando o pais for completo
        acertou = ''.join(letras_certas)
        if(acertou == pais_secreto):
                print(" Parabéns, você ganhou! ")
                print("       ___________      ")
                print("      '._==_==_=_.'     ")
                print("      .-\ \:      /-.    ")
                print("     | (|:.     |) |    ")
                print("      '-|:.     |-'     ")
                print("        \ \::.    /      ")
                print("         '::. .'        ")
                print("           ) (          ")
                print("         _.' '._        ")
                print("        '-------'       ")
                break
        # Metodo para desenhar a Forca

        if(tentativas == 1):
            print(" |      |    ")
            print(" |      |    ")
            print(" |     (_)   ")
            print(" |           ")
            print(" |           ")
            print(" |           ")

        if (tentativas == 2):
            print("  _______    ")
            print(" |/     |    ")
            print(" |     (_)   ")
            print(" |     \     ")
            print(" |           ")
            print(" |           ")

        if (tentativas == 3):
            print("  _______    ")
            print(" |/     |    ")
            print(" |     (_)   ")
            print(" |     \|    ")
            print(" |           ")
            print(" |           ")

        if (tentativas == 4):
            print("  _______    ")
            print(" |/     |    ")
            print(" |     (_)   ")
            print(" |     \|/   ")
            print(" |           ")
            print(" |           ")

        if (tentativas == 5):
            print("  _______    ")
            print(" |/     |    ")
            print(" |     (_)   ")
            print(" |     \|/   ")
            print(" |      |     ")
            print(" |           ")

        if (tentativas == 6):
            print("  _______    ")
            print(" |/     |    ")
            print(" |     (_)   ")
            print(" |     \|/   ")
            print(" |      |    ")
            print(" |     /     ")

        if (tentativas == 7):
            print("  _______    ")
            print(" |/     |    ")
            print(" |     (_)   ")
            print(" |     \|/   ")
            print(" |      |    ")
            print(" |     / \   ")
            print(" |           ")
            print(" | Enforcado ")

if(__name__ == "__main__"):
    jogar()







