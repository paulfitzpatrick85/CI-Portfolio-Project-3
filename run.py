import random


def welcome_message():
    """Welcome user to game upon loading"""
    print("""-------------------------------\n 
     Welcome to HangMan!
     The program will select a word at random.
     Your job is to guess, one letter at a time, 
     what that word is.
     With each incorrect answercthe hangman will
     appear one body part at a time.
     \n-------------------------------""")


def initiate_game():
    """Ask user if they would like to start a new game"""
    name = input("Input your name:").lower()
    print(f"{name}, would you like to play a new game?") 
    start_game_question = input("Type 'y' for yes or 'n' for no.\n").lower()
    if start_game_question == "y":
        print("start_game function to be called")
        #start_game() function to be built next
    elif start_game_question == "n":
        print("Okay, we'll return to the start and begin  when ready")
        main()
    else:
        print("please enter 'y' or 'n'")
        initiate_game()
        

def main():
    """Main function to hold all functions"""
    welcome_message()
    initiate_game()


main()




