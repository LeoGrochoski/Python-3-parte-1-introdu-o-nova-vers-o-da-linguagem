# import random

# Python 3 parte 1: Introdução à nova versão da linguagem

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

# print(34*"'")
# print("|  Welcome to the Guessing Game  | ")
# print(34*"'")

# Criando e selecionando o numero secreto de forma randomica com a lib "random" e a função .random()
# .random() cria numeros de 0.0 a 1.0
# secret_number = round(random.random() * 50)

# Criando e selecionando o numero secreto de forma randomica
# secret_number = random.randrange(1, 51)
#
# total_try = 5
#
# print("What is the secret number?")
#
# for turn in range(1, total_try + 1):
#     print(f"Round {turn} of {total_try} rounds")
#     shot_str = input("Choose a number between 1 and 50?")
#     shot = int(shot_str)
#     if(shot < 1 or shot > 50):
#         print("Invalid, you must to choose a number between 1 and 50. Unfurtunately you lost a choice")
#         continue
#     if(shot == secret_number):
#         print("Amazing! You got it right")
#         break
#     else:
#             if(shot > secret_number and turn < 5):
#                 print("Too bad, but you were wrong. The secret number is smaller.")
#             elif(shot < secret_number and turn < 5):
#                 print("Too bad, but you were wrong. The secret number is bigger.")
#             elif(shot > secret_number or shot < secret_number and total_try >= 5):
#                 print("Sorry, but you were wrong. The game is over.")


# 5 - Criando jogo com level de dificuldade onde o jogador for avançando vai reduzindo o numero de tentativas
# Implmentado sistema de loop para os leveis e incluido os rounds de tentativas por dificuldade
# Criando e selecionando o numero secreto de forma randomica usando a lib "random" e a função .randrange()

# print("*********************************")
# print("Welcome to the Guessing Game!")
# print("*********************************")
#
# secret_number = random.randrange(1, 101)
# total_try = 0
# points = 1000
#
# print("Qual o nível de dificuldade?")
# print("(1) Fácil (2) Médio (3) Difícil")
#
# level = int(input("Defina o nível: "))
#
# if(level == 1):
#     total_try = 20
# elif(level == 2):
#     total_try = 10
# else:
#     total_try = 5
#
# for turn in range(1, total_try + 1):
#     print("Tentativa {} de {}".format(turn, total_try))
#
#     shot_str = input("Digite um número entre 1 e 100: ")
#     print("Você digitou ", shot_str)
#     shot = int(shot_str)
#
#     if(shot < 1 or shot > 100):
#         print("Você deve digitar um número entre 1 e 100!")
#         continue
#
#     right = shot == secret_number
#     bigger = shot > secret_number
#     smaller = shot < secret_number
#
#     if(right):
#         print("Você acertou e fez {} pontos!".format(points))
#         break
#     else:
#         if(bigger):
#             print("Você errou! O seu chute foi maior do que o número secreto.")
#         elif(smaller):
#             print("Você errou! O seu chute foi menor do que o número secreto.")
#         lost_points = abs(secret_number - shot)
#         points = points - lost_points
#
# print("Fim do jogo")

# 6 - Para declarar uma função, devemos usar a palavra chave def
# tod0 codigo identado faz parte da função:
#   def nome_da_funcao():
#   print("aprendendo funções")

# Uma função também pode receber parâmetros e retornar algum valor
# def soma(a, b):
#     return a + b

# -------------------------------------- NOVO CURSO --------------------------------------------------------

# Python 3 parte 2: Avançando na linguagem

# 1 - Criando um loop para verificação da letra

# def play():
#     print(25*"/")
#     print("/   Jogo da Forca    / ")
#     print(25*"/")
#
#     secret_country = "brasil"
#     hanged = False
#     escaped = False
#
#     while(not hanged and not escaped):
#         print("jogando jogo da forca" "\n")
#         print("Qual o pais? _ _ _ _ _ _")
#         shot = input("digite uma letra: ")
#         if(shot in secret_country):
#             print(f"tem a letra {shot}, no pais")
#         else:
#             print(f"não tem a letra {shot}, no pais!")
#
#     print("Game Over")

# 2 - encontrando letras dentro da string
# palavra = "aluracursos" / palavra.find("b"), o resultado será -1, pois quando a busca nada encontra sempre é -1
# .casefold() faz tratamento de letras maiusculas em minusculas semelhante ao .lower(), removendo todas as distinçoes
# função ".strip" retira os espaços em brancos da string
# função .index(), que nos retorna o índice da primeira ocorrência de um determinado elemento em uma lista
# jeito fácil de contar o número de ocorrências de um determinado elemento em uma lista é a função .count()

# def play():
#     print(25*"/")
#     print("/   Jogo da Forca    / ")
#     print(25*"/")
#
#     palavra_secreta = "banana"
#     letras_acertadas = ["_", "_", "_", "_", "_", "_"]
#
#     enforcou = False
#     escapou = False
#
#     while(not enforcou and not escapou):
#
#         chute = input("Qual a letra? ")
#         chute = chute.strip()
#
#         posicao = 0
#         for letra in palavra_secreta:
#             if(chute.upper() == letra.upper()):
#                 letras_acertadas[posicao] = letra
#             posicao = posicao + 1
#
#         print(letras_acertadas)

# if(__name__ == "__main__"):
#     play()

# # 3 - Tuplas e Listas
# # Podedmos alterar listas adicionando elementos utilizando a função: .append
# # A função .pop deleta o ultimo elemento da lista
# # Tupla é uma estrutura (lista) de dados imutavel, não podedmos alterar

# # Tupla com numeros que podem ser cordenadas de eixo x e y

# # Exemplo 1

# p1 = (3,5)
# p2 = (3,6)
# p3 = (5,7)
# line = [p1, p2, p3]
# print(line, "\n")

# # ---------------------------------------------------------------------------------------
# # Exemplo 2

# # Tupla com nome que podem ser de instrutores,
# # depois conseguimos chamar as tuplas pela lista de instrutores e sua posição

# p1 = ("Leo", 27)
# p2 = ("Je", 26)
# instrutores = [p1, p2]
# print(instrutores, "\n")
# print(instrutores[0])
# print(instrutores[1])

# também podemos acessar uma informação de forma unica selecionando a tupla e depois a variavel nome e idade por exemplo

# print(f" O instrutor {instrutores[0][0]} tem {instrutores[0][1]} anos")

# # ---------------------------------------------------------------------------------------

# # Converter uma lista em tupla

# # listas são criadas utilizando [] e pode ser editada
# lista = []
# lista.append("Leonardo")
# lista.append("José")
# lista.append("Maria")
# lista.append("Rafaela")
# print(lista)
#
# # Convertemos a lista em tupla utilizando a função built-in tuple, tuplas são definadas por ()
#
# nova_lista = tuple(lista)
#
# # A lista agora é uma tupla que é imutavel
# print(nova_lista)
#
# # Para convertermos uma tupla em lista podemos utilizara função list
#
# outra_lista = list(nova_lista)
# print(outra_lista)

# Evitando elementos duplicados em nossa sequencia, podemos utilizar o set
# set = {11111, 00000, 10101}

# Para adicionar um elemento a uma coleção set, deve-se utilizar o .add e não mais o .append, e se este elemento for
# repetido ele não será adicionado

# Exemplo
# coleção = {11111, 22222, 33333}
# coleção.add(11111)
# print(coleção)
# print(coleção[0])

# Conhecendo o dictionary
# Se não conhecemos a localização de um elemento dentro da lista e precisamos de uma informação dentro dela,
# pode-se utilizar o metodo de busca através do nome, só que isso não vai funcionar com lista

# Para criar um dicionário devemos inicializar os instrutores de um modo um pouco diferente

# Exemplo
# instrutores = {'Leonardo' : 27, 'João' : 32, 'Rafael' : 36}

# No lado ésquerdo fica a chave e no lado direito o valor, é importante pois utiliza-se a chave para buscar o valor

# Agora podemos buscar a informação

# instrutores['Leonardo']

# List Comprehension Desafio

# inteiros = [1,3,4,5,7,8,9]
# pares = []
# for numero in inteiros:
#     if numero % 2 == 0:
#         pares.append(numero)
#

inteiros = [1,3,4,5,7,8,9]
print(f"Está é a lista de numeros inteiros: {inteiros}")
pares = [num for num in inteiros if num % 2 == 0]
print(f"Está é a lista com apenas os numeros pares: {pares}")

