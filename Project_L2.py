import random

def game_intro():
    print("Yo! Welcome to the Mysterious Forest Adventure!")
    print("You’ve found yourself in a spooky forest. The goal? Get out of here alive and with the highest score possible.")
    print("Be careful though, weird stuff is happening all around.\n")

def choose_path():
    print("You see two paths ahead:")
    print("1. Go left")
    print("2. Go right")
    choice = input("Which path do you pick? (1 or 2): ")
    while choice not in ["1", "2"]:
        choice = input("Come on, you gotta pick 1 or 2: ")
    return int(choice)

def encounter(choice):
    if choice == 1:
        event = random.choice(["wild animal", "abandoned hut", "trap"])
        if event == "wild animal":
            print("Uh-oh! A wild animal jumps out and attacks you!")
            return "lose", -10
        elif event == "abandoned hut":
            print("You find a creepy abandoned hut with some useful stuff inside.")
            return "continue", 5
        elif event == "trap":
            print("Oh no! You stepped into a trap and can’t get out.")
            return "lose", -10
    else:
        event = random.choice(["hidden treasure", "dead end", "friendly guide"])
        if event == "hidden treasure":
            print("Score! You found hidden treasure! You win!")
            return "win", 20
        elif event == "dead end":
            print("Bummer, it’s a dead end. You have to turn back.")
            return "continue", 0
        elif event == "friendly guide":
            print("Nice! A friendly guide helps you find the way out. You win!")
            return "win", 20

def play_again():
    choice = input("Wanna play again? (yes or no): ")
    while choice not in ["yes", "no"]:
        choice = input("Just type 'yes' or 'no': ")
    return choice == "yes"

def play_game():
    game_intro()
    game_over = False
    score = 0
    while not game_over:
        choice = choose_path()
        result, points = encounter(choice)
        score += points
        if result == "win":
            game_over = True
            print(f"Congrats, you made it out of the forest! Your final score is: {score}")
        elif result == "lose":
            game_over = True
            print(f"Game over. Better luck next time. Your final score is: {score}")
        elif result == "continue":
            print("You keep moving through the forest.\n")
        if game_over and play_again():
            game_over = False
            score = 0
            print("\nStarting a new game...\n")
        elif game_over:
            print("Thanks for playing the Mysterious Forest Adventure!")

if __name__ == "__main__":
    play_game()
