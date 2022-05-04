import random

# print(36*"*")
# print("  Bem vindo no jogo de adivinhação! ")
# print(36*"*")
#
# numero_secreto = 43

# 1 - Codigo simples de IF referente a comparação de variaveis, jogo de advinhação
# IF -> Serve para testar uma condição e executar um bloco uma única vez.

# if(numero_secreto == chute):
#     print("Você digitou", chute, "Parabéns! Você Acertou!")
# else:
#     print("Você digitou", chute, "Que pena! Você Errou! Tente novamente")


# 2 - Codigo um pouco mais complexo com IF e ELIF referente a comparação de variaveis, jogo de advinhação

# chute_str = input("Digite o seu numer: ")
#
# print("Você digitou", chute_str)
# chute = int(chute_str)
#
# acertou = chute == numero_secreto
# maior = chute > numero_secreto
# menor = chute < numero_secreto
#
# if(acertou):
#     print("Você acertou!")
# else:
#     if(maior):
#         print("Você errou, seu chute foi maior que o numero secreto")
#     elif(menor):
#         print("Você errou, seu chute foi menor que o numero secreto")


# 3 - Codigo completo com WHILE, IF e ELIF, com 3 tentativas de resposta e dica de maior ou menor
# IF e WHILE -> Ambos possuem uma condição de entrada.
# WHILE -> Serve para testar uma condição e executar um bloco enquanto a condição for verdadeira.
# BREAK é uma função que para o laço de repetição encerrando o loop.
# PYTHON não não tem uma estrutura condicional como a do-while.

# tentativa = 0
# rodada = 1
# total_rodada = 3
#
# while tentativa <= 2:
#     print(f"Tentativa {rodada} de {total_rodada}")
#     chute_str = input("Digite o seu numero: ")
#     chute = int(chute_str)
#     if chute == numero_secreto:
#         print("Parabéns! Você acertou.")
#         break
#     else:
#         if chute > numero_secreto:
#             print("Errado! O numero secreto é menor que seu chute, tente novamente.")
#         elif chute < numero_secreto:
#             print("Errado! O numero secreto é maior que seu chute, tente novamente.")
#     tentativa = tentativa + 1
#     rodada = rodada + 1
# if tentativa > 2 and chute != numero_secreto:
#     print("Fim de Jogo")


# 4 - Loop utilizando FOR
# Para utilizar o FOR é preciso declarar a variavel + in + range() e dentro selecionar o intervalo do loop:
# for var in rage(0,10)
# CONTINUE é uma função que mantem o laço de repetição somente pulando para o proximo loop
# Utilizando a biblioteca "random" para gerar o numero secreto com a função .randrange

print(34*"'")
print("|  Welcome to the Guessing Game  | ")
print(34*"'")

print("What is the secret number?")

# Criando e selecionando o numero secreto de forma randomica com a lib "random" e a função .random()
# .random() cria numeros de 0.0 a 1.0
# secret_number = round(random.random() * 50)

# Criando e selecionando o numero secreto de forma randomica usando a lib "random" e a função .randrange()
secret_number = random.randrange(1, 51)

max_level = 3
easy_max_turn = 5
medium_max_turn = 4
hard_max_turn = 3
level = 1

invalid_shot = ""
right_shot = ""
wrong_shot = ""

for level in range(1, max_level + 1):
    if (level == 1):
        level = "Easy"
        if (level == "Easy"):
            print(f"The player is in the {level} level")
        for turn in range(1, easy_max_turn + 1):
            print(f"Round {turn} of {easy_max_turn} rounds")
            shot_str = input("Choose a number between 1 and 50?")
            shot = int(shot_str)
            if (shot < 1 or shot > 50):
                print("Invalid, you must to choose a number between 1 and 50. Unfurtunately you lost a choice")
                continue
            if (shot == secret_number):
                print("Amazing! You got it right!")
                break
            elif (shot > secret_number and turn < 5):
                print("Too bad, but you were wrong. The secret number is smaller.")
            elif (shot < secret_number and turn < 5):
                print("Too bad, but you were wrong. The secret number is bigger.")
        if(shot > secret_number or shot < secret_number and easy_max_turn >= 5):
            print(f"Sorry, but you were wrong. The secret number was {secret_number}. The game is over.")
            break
        else:
            continue
    elif (level == 2):
        level = "Medium"
        if (level == "Medium"):
            print(f"The player is in the {level} level")
            for turn in range(1, medium_max_turn + 1):
                print(f"Round {turn} of {medium_max_turn} rounds")
                shot_str = input("Choose a number between 1 and 50?")
                shot = int(shot_str)
                if (shot < 1 or shot > 50):
                    print("Invalid, you must to choose a number between 1 and 50. Unfurtunately you lost a choice")
                    continue
                if (shot > secret_number and turn < 5):
                    print("Too bad, but you were wrong. The secret number is smaller.")
                elif (shot < secret_number and turn < 5):
                    print("Too bad, but you were wrong. The secret number is bigger.")
                elif (shot > secret_number or shot < secret_number and medium_max_turn >= 5):
                    print(f"Sorry, but you were wrong. The secret number was {secret_number}. The game is over.")
                    break
                elif (shot == secret_number):
                    print("Amazing! You got it right!")
                    break
    else:
        level = "Hard"
        if (level == "Hard"):
            for turn in range(1, hard_max_turn + 1):
                print(f"Round {turn} of {hard_max_turn} rounds")
                shot_str = input("Choose a number between 1 and 50?")
                shot = int(shot_str)
                if (invalid_shot == shot < 1 or shot > 50):
                    print("Invalid, you must to choose a number between 1 and 50. Unfurtunately you lost a choice")
                    continue
                if (right_shot == secret_number):
                    print("Amazing! You got it right!")
                    break
                else:
                    if (shot > secret_number and turn < 5):
                        print("Too bad, but you were wrong. The secret number is smaller.")
                    elif (shot < secret_number and turn < 5):
                        print("Too bad, but you were wrong. The secret number is bigger.")
                    elif (wrong_shot == shot > secret_number or shot < secret_number and hard_max_turn >= 5):
                        print(f"Sorry, but you were wrong. The secret number was {secret_number}. The game is over.")
