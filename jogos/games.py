import guessing_game
import hangman_game

print(25*"*")
print("*   Choose Your Game    * ")
print(25*"*", "\n")

print("(1) to The Guessing Game (2) to The Hangman Game")

game = int(input("Choose the Game: "))

if(game == 1):
    print("Playing the Guessing Game")
    guessing_game.play()
elif(game == 2):
    print("Playing The Hangman Game")
    hangman_game.play()
