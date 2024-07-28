import random
import time

# Prints a message and pauses for a specified amount of time.
def print_pause(message, delay=1):
    print(message)
    time.sleep(delay)

# Introduces the game and explains the goal to the player.
def game_intro():
    print_pause("Yo! Welcome to the Mysterious Forest Adventure!")
    print_pause("You’ve found yourself in a spooky forest. The goal? Get out of here")
    print_pause("alive and with the highest score possible. Be careful though, weird")
    print_pause("stuff is happening all around.")
    print_pause("The game ends when you reach a score of 20 points.")
    print_pause("Good luck!\n")

# Prompts the player to choose a path and validates the input.
def choose_path():
    print("You see two paths ahead:")
    print("1. Go left")
    print("2. Go right")
    choice = input("Which path do you pick? (1 or 2): ")
    while choice not in ["1", "2"]:
        choice = input("Come on, you gotta pick 1 or 2: ")
    return int(choice)

# Determines the encounter based on the player's choice.
def encounter(choice):
    if choice == 1:
        event = random.choice(["wild animal", "abandoned hut", "trap"])
        if event == "wild animal":
            print_pause("Uh-oh! A wild animal jumps out and attacks you!")
            return "lose", -10
        elif event == "abandoned hut":
            print_pause("You find a creepy abandoned hut with some useful stuff inside.")
            return "continue", 5
        elif event == "trap":
            print_pause("Oh no! You stepped into a trap and can’t get out.")
            return "lose", -10
    else:
        event = random.choice(["hidden treasure", "dead end", "friendly guide"])
        if event == "hidden treasure":
            print_pause("Score! You found hidden treasure! You win!")
            return "win", 20
        elif event == "dead end":
            print_pause("Bummer, it’s a dead end. You have to turn back.")
            return "continue", 0
        elif event == "friendly guide":
            print_pause("Nice! A friendly guide helps you find the way out. You win!")
            return "win", 20

# Prompts the player to play again or exit the game and validates the input.
def play_again():
    choice = input("Wanna play again? (yes or no): ").lower()
    while choice not in ["yes", "no"]:
        choice = input("Just type 'yes' or 'no': ")
    return choice == "yes"

# Main function to play the game, handles game loop and game over conditions.
def play_game():
    game_intro()
    game_over = False
    score = 0
    while not game_over:
        choice = choose_path()
        result, points = encounter(choice)
        score += points
        print_pause(f"Current score: {score}")
        if score >= 20:
            game_over = True
            print_pause(f"Congrats, you made it out of the forest! Your final score is: {score}")
        elif result == "lose":
            game_over = True
            print_pause(f"Game over. Better luck next time. Your final score is: {score}")
        elif result == "continue":
            print_pause("You keep moving through the forest.\n")
        if game_over and play_again():
            game_over = False
            score = 0
            print_pause("\nStarting a new game...\n")
        elif game_over:
            print_pause("Thanks for playing the Mysterious Forest Adventure!")

if __name__ == "__main__":
    play_game()






# The Above Code The comments above function







import random
import time


def print_pause(message, delay=1):
    """
    Prints a message and pauses for a specified amount of time.

    :param message: str - The message to be printed.
    :param delay: int - The time in seconds to pause after printing the message.
    """
    print(message)
    time.sleep(delay)


def game_intro():
    """
    Introduces the game and explains the goal to the player.
    """
    print_pause("Yo! Welcome to the Mysterious Forest Adventure!")
    print_pause("You’ve found yourself in a spooky forest. The goal? Get out of here")
    print_pause("alive and with the highest score possible. Be careful though, weird")
    print_pause("stuff is happening all around.")
    print_pause("The game ends when you reach a score of 20 points.")
    print_pause("Good luck!\n")


def choose_path():
    """
    Prompts the player to choose a path and validates the input.

    :return: int - The chosen path (1 or 2).
    """
    print("You see two paths ahead:")
    print("1. Go left")
    print("2. Go right")
    choice = input("Which path do you pick? (1 or 2): ")
    while choice not in ["1", "2"]:
        choice = input("Come on, you gotta pick 1 or 2: ")
    return int(choice)


def encounter(choice):
    """
    Determines the encounter based on the player's choice.

    :param choice: int - The path chosen by the player.
    :return: tuple - The result of the encounter and the points gained/lost.
    """
    if choice == 1:
        event = random.choice(["wild animal", "abandoned hut", "trap"])
        if event == "wild animal":
            print_pause("Uh-oh! A wild animal jumps out and attacks you!")
            return "lose", -10
        elif event == "abandoned hut":
            print_pause("You find a creepy abandoned hut with some useful stuff inside.")
            return "continue", 5
        elif event == "trap":
            print_pause("Oh no! You stepped into a trap and can’t get out.")
            return "lose", -10
    else:
        event = random.choice(["hidden treasure", "dead end", "friendly guide"])
        if event == "hidden treasure":
            print_pause("Score! You found hidden treasure! You win!")
            return "win", 20
        elif event == "dead end":
            print_pause("Bummer, it’s a dead end. You have to turn back.")
            return "continue", 0
        elif event == "friendly guide":
            print_pause("Nice! A friendly guide helps you find the way out. You win!")
            return "win", 20


def play_again():
    """
    Prompts the player to play again or exit the game and validates the input.

    :return: bool - True if the player wants to play again, False otherwise.
    """
    choice = input("Wanna play again? (yes or no): ").lower()
    while choice not in ["yes", "no"]:
        choice = input("Just type 'yes' or 'no': ")
    return choice == "yes"


def play_game():
    """
    Main function to play the game, handles game loop and game over conditions.
    """
    game_intro()
    game_over = False
    score = 0
    while not game_over:
        choice = choose_path()
        result, points = encounter(choice)
        score += points
        print_pause(f"Current score: {score}")
        if score >= 20:
            game_over = True
            print_pause(f"Congrats, you made it out of the forest! Your final score is: {score}")
        elif result == "lose":
            game_over = True
            print_pause(f"Game over. Better luck next time. Your final score is: {score}")
        elif result == "continue":
            print_pause("You keep moving through the forest.\n")
        if game_over and play_again():
            game_over = False
            score = 0
            print_pause("\nStarting a new game...\n")
        elif game_over:
            print_pause("Thanks for playing the Mysterious Forest Adventure!")


if __name__ == "__main__":
    play_game()
