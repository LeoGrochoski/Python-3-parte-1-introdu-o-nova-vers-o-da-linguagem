import random


def play():
    print(34*"'")
    print("|  Welcome to the Guessing Game  | ")
    print(34*"'", "\n")

    # Variaveis de loop
    max_level = 3
    easy_max_turn = 7
    medium_max_turn = 5
    hard_max_turn = 3

    # Variaveis de pontuação
    easy_points = 35
    medium_points = 35
    hard_points = 35
    bonus = 15
    total_points = 0

    print("Let's Play?", "\n")
    print("What is the secret number?", "\n")

    for level in range(1, max_level + 1):
        secret_number = random.randrange(1, 51)
        if (level == 1):
            level = "Easy"
            if (level == "Easy"):
                print(f"The player is in the {level} level", "\n")
            for turn in range(1, easy_max_turn + 1):
                print(f"Round {turn} of {easy_max_turn} rounds", "\n")
                shot_str = input("Choose a number between 1 and 50?")
                shot = int(shot_str)
                if (shot < 1 or shot > 50):
                    print("Invalid, you must to choose a number between 1 and 50. Unfurtunately you lost a choice", "\n")
                    continue
                if (shot == secret_number):
                    if (shot == secret_number and turn == 1):
                        easy_points = easy_points - 0
                    elif (shot == secret_number and turn == 2):
                        easy_points = easy_points - 5
                    elif (shot == secret_number and turn == 3):
                        easy_points = easy_points - 10
                    elif (shot == secret_number and turn == 4):
                        easy_points = easy_points - 15
                    elif (shot == secret_number and turn == 5):
                        easy_points = easy_points - 20
                    elif (shot == secret_number and turn == 6):
                        easy_points = easy_points - 25
                    elif (shot == secret_number and turn == 7):
                        easy_points = easy_points - 30
                    else:
                        easy_points = easy_points - 35
                    total_points = easy_points + bonus
                    print(f"Amazing! You got it right! You have {total_points} points. You are going to the next level", "\n", "\n")
                    break
                elif (shot > secret_number and turn < 7):
                    print("Too bad, but you were wrong. The secret number is smaller.", "\n")
                elif (shot < secret_number and turn < 7):
                    print("Too bad, but you were wrong. The secret number is bigger.", "\n")
            if(shot > secret_number or shot < secret_number and easy_max_turn >= 7):
                print(f"Sorry, but you were wrong. The secret number was {secret_number}. The game is over.", "\n")
                break
            else:
                continue
        elif (level == 2):
            level = "Medium"
            if (level == "Medium"):
                print(f"The player is in the {level} level")
            for turn in range(1, medium_max_turn + 1):
                print(f"Round {turn} of {medium_max_turn} rounds", "\n")
                shot_str = input("Choose a number between 1 and 50?")
                shot = int(shot_str)
                if (shot < 1 or shot > 50):
                    print("Invalid, you must to choose a number between 1 and 50. Unfurtunately you lost a choice", "\n", "\n")
                    continue
                if(shot == secret_number):
                    if (shot == secret_number and turn == 1):
                        medium_points = medium_points - 0
                        print(medium_points)
                    elif (shot == secret_number and turn == 2):
                        medium_points = medium_points - 7
                    elif (shot == secret_number and turn == 3):
                        medium_points = medium_points - 14
                    elif (shot == secret_number and turn == 4):
                        medium_points = medium_points - 21
                    elif (shot == secret_number and turn == 5):
                        medium_points = medium_points - 28
                    else:
                        medium_points = medium_points - 35
                    total_points = easy_points + medium_points + (2 * bonus)
                    print(f"Amazing! You got it right! You have {total_points} points. You are going to the next level", "\n", "\n")
                    break
                elif (shot > secret_number and turn < 5):
                    print("Too bad, but you were wrong. The secret number is smaller.", "\n")
                elif (shot < secret_number and turn < 5):
                    print("Too bad, but you were wrong. The secret number is bigger.", "\n")
            if(shot > secret_number or shot < secret_number and medium_max_turn >= 5):
                print(f"Sorry, but you were wrong. The secret number was {secret_number}. You had {total_points}"
                      f" points. The game is over.", "\n")
                break
            else:
                continue
        elif(level == 3):
            level = "Hard"
            if (level == "Hard"):
                print(f"The player is in the {level} level")
            for turn in range(1, hard_max_turn + 1):
                print(f"Round {turn} of {hard_max_turn} rounds", "\n")
                shot_str = input("Choose a number between 1 and 50?")
                shot = int(shot_str)
                if (shot == shot < 1 or shot > 50):
                    print("Invalid, you must to choose a number between 1 and 50. Unfurtunately you lost a choice",
                          "\n")
                    continue
                if (shot == secret_number):
                    if (shot == secret_number and turn == 1):
                        hard_points = hard_points - 0
                    elif (shot == secret_number and turn == 2):
                        hard_points = hard_points - 12
                    elif (shot == secret_number and turn == 3):
                        hard_points = hard_points - 23
                    else:
                        hard_points = hard_points - 35
                    total_points = easy_points + medium_points + hard_points + (3 * bonus)
                    print(f"Amazing! You got it right! You did {total_points} points. Congratulations!!!", "\n")
                    break
                elif(shot > secret_number and turn < 3):
                    print("Too bad, but you were wrong. The secret number is smaller.", "\n")
                elif (shot < secret_number and turn < 3):
                    print("Too bad, but you were wrong. The secret number is bigger.", "\n")
            if (shot == shot > secret_number or shot < secret_number and hard_max_turn >= 3):
                print(f"Sorry, but you were wrong. The secret number was {secret_number}. You had {total_points}"
                      f" points. The game is over.", "\n")


if(__name__ == "__main__"):
    play()
