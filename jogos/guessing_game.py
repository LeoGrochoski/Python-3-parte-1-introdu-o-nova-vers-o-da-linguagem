import random

print(34*"'")
print("|  Welcome to the Guessing Game  | ")
print(34*"'")

print("What is the secret number?")

# Variaveis de loop
max_level = 3

easy_max_turn = 7
medium_max_turn = 5
hard_max_turn = 3

level = 1

for level in range(1, max_level + 1):
    secret_number = random.randrange(1, 51)
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
            elif (shot > secret_number and turn < 7):
                print("Too bad, but you were wrong. The secret number is smaller.")
            elif (shot < secret_number and turn < 7):
                print("Too bad, but you were wrong. The secret number is bigger.")
        if(shot > secret_number or shot < secret_number and easy_max_turn >= 7):
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
            if(shot == secret_number):
                print("Amazing! You got it right!")
                break
            elif (shot > secret_number and turn < 5):
                print("Too bad, but you were wrong. The secret number is smaller.")
            elif (shot < secret_number and turn < 5):
                print("Too bad, but you were wrong. The secret number is bigger.")
        if(shot > secret_number or shot < secret_number and medium_max_turn >= 5):
                print(f"Sorry, but you were wrong. The secret number was {secret_number}. The game is over.")
                break
        else:
            continue
    elif(level == 3):
        level = "Hard"
        if (level == "Hard"):
            print(f"The player is in the {level} level")
        for turn in range(1, hard_max_turn + 1):
            print(f"Round {turn} of {hard_max_turn} rounds")
            shot_str = input("Choose a number between 1 and 50?")
            shot = int(shot_str)
            if (shot == shot < 1 or shot > 50):
                print("Invalid, you must to choose a number between 1 and 50. Unfurtunately you lost a choice")
                continue
            if (shot == secret_number):
                print("Amazing! You got it right!")
                break
            else:
                if (shot > secret_number and turn < 3):
                    print("Too bad, but you were wrong. The secret number is smaller.")
                elif (shot < secret_number and turn < 3):
                    print("Too bad, but you were wrong. The secret number is bigger.")
        if (shot == shot > secret_number or shot < secret_number and hard_max_turn >= 3):
                print(f"Sorry, but you were wrong. The secret number was {secret_number}. The game is over.")