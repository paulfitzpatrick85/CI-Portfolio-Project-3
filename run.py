import random


def welcome_message():
    """Welcome user to game upon loading"""
    print("""   -------------------------------------------------\n 
     *********** Welcome to HangMan! ************\n
     The program will select a word at random.
     Your job is to guess, one letter at a time, 
     what that word is.
     With each incorrect answercthe hangman will
     appear one body part at a time.
     \n   -------------------------------------------------""")


def initiate_game():
    """Ask user if they would like to start a new game"""
    name = input("Input your name:").lower().capitalize()
    print(f"{name}, would you like to play a new game?") 
    start_game_question = input("Type 'y' for yes or 'n' for no.\n").lower()
    if start_game_question == "y":
        print(f"Great {name}, lets begin!")
    elif start_game_question == "n":
        print("Okay, we'll return to the start and begin  when ready")
        main()
    else:
        print("please enter 'y' or 'n'")
        initiate_game()


def start_game():
    """starts game by first selecting random word from list,
    then asks user to guess letter or whole word"""

    words = ["roof", "five", "four", "ball", "room"]
    word = random.choice(words).lower()
    print("A word has been selected")
    print(word)
    letter = input("guess a letter:")
    if letter in word:
        print(f"{letter} is in there!")
    else:
        print(f"{letter} ain't there sorry!")
#         print(r"""  +---+
#   |   |
#       |
#       |
#       |
#       |
# =========""")
  

def main():
    """Main function to hold all functions"""
    welcome_message()
    initiate_game()
    start_game() 


main()




