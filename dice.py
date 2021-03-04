# What to do:  make a basic python dice simulator that can be used in the terminal (no graphics required)
# Algorithm
# 1. Make dice
# 2. Develop a random number
# 3. Check the number
# 4. Print the die face
# 3. Loop so that you can roll again and again

# imports the random module
import random
from sys import exit
# Prints the opening credits
print("This is Jackson Detke's dice simulator game")
print("Completed as part of the Python 3 Complete Bootcamp Master Course: Build 15+ Projects and Games on StackSkills")

# Creates the dice simulator function with "user_input" as the argument
def dice_simulator(user_input):
    # Asks initially if you want to play
    user_input = input("Type y if you want to play.")
    # Runs the program again as long as user input is entered in
    # so that "user_input" exists
    while user_input:
        # Generates two random integers between 1 and 6
        die_number_1 = random.randint(1, 6)
        die_number_2 = random.randint(1, 6)
        # Plays the game if "user_input" is equal to "y"
        if user_input == "y":
            # Prints the appropriate dice depending on the integers generated
            if die_number_1 == 1:
                print("-----------")
                print("|         |")
                print("|    O    |")
                print("|         |")
                print("-----------")
            elif die_number_1 == 2:
                print("-----------")
                print("|  O      |")
                print("|         |")
                print("|      O  |")
                print("-----------")
            elif die_number_1 == 3:
                print("-----------")
                print("|  O      |")
                print("|    O    |")
                print("|      O  |")
                print("-----------")
            elif die_number_1 == 4:
                print("-----------")
                print("|  O   O  |")
                print("|         |")
                print("|  O   O  |")
                print("-----------")
            elif die_number_1 == 5:
                print("-----------")
                print("|  O   O  |")
                print("|    O    |")
                print("|  O   O  |")
                print("-----------")
            elif die_number_1 == 6:
                print("-----------")
                print("|  O   O  |")
                print("|  O   O  |")
                print("|  O   O  |")
                print("-----------")
            if die_number_2 == 1:
                print("-----------")
                print("|         |")
                print("|    O    |")
                print("|         |")
                print("-----------")
            elif die_number_2 == 2:
                print("-----------")
                print("|  O      |")
                print("|         |")
                print("|      O  |")
                print("-----------")
            elif die_number_2 == 3:
                print("-----------")
                print("|  O      |")
                print("|    O    |")
                print("|      O  |")
                print("-----------")
            elif die_number_2 == 4:
                print("-----------")
                print("|  O   O  |")
                print("|         |")
                print("|  O   O  |")
                print("-----------")
            elif die_number_2 == 5:
                print("-----------")
                print("|  O   O  |")
                print("|    O    |")
                print("|  O   O  |")
                print("-----------")
            elif die_number_2 == 6:
                print("-----------")
                print("|  O   O  |")
                print("|  O   O  |")
                print("|  O   O  |")
                print("-----------")
            # Adds together the individual dice numbers and prints the total dice number
            total = die_number_1 + die_number_2
            print(f"You rolled a {total}!")
            # Asks if you want to play again, this changes "user_input"
            user_input = input("Type y if you want to roll again.")
        # Stops the game and prints the closing statement if you type in a user input other than "y"
        else:
            print("Bye, thanks for checking out my game!")
            exit()
# Calls the function so the game can be played
dice_simulator("y")