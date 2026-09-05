'''
We are making a Snake Water Gun game.

Rules:
Snake Vs Water = Snake wins
Water Vs Gun = Water Wins
Gun Vs Snake = Gun Wins
Same Choice = Draw
'''
import random

print("Welcome to the Snake, Water & Gun game")

while True:
    start = input("Please press Enter to start: ")
    if start == "":
        print("\nGame Started!")
        break
    else:
        print("You pressed the wrong button, Please try again\n")

computer_choices_list = ["g", "w", "s"]
input_options = {"w": "Water", "g": "Gun", "s": "Snake"}

while True:  
    while True:
        user_input = input("Choose one between 'w' , 'g' , 's' : ").lower()
        if user_input in ("w", "g", "s"):
            break
        else:
            print("Wrongfully entered, Please try again !\n")

    user_choice = input_options[user_input]
    computer_choice = input_options[random.choice(computer_choices_list)]

    print(f"\nYou have chosen {user_choice}")
    print(f"Computer has chosen {computer_choice}\n")

    if user_choice == computer_choice:
        print("There is a tie!")
    elif (user_choice, computer_choice) in [("Snake", "Water"), ("Water", "Gun"), ("Gun", "Snake")]:
        print("You have won the game, congratulations!")
    else:
        print("You have lost the game, Computer wins!!")

    # Ask whether to play again
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing! Goodbye.")
        break