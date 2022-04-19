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


def get_words():
    words = ["roof", "five", "four", "ball", "room"]
    return random.choice(words).lower()


guess = False


def start_game():
    """starts game by first selecting random word from list,
    then asks user to guess letter or whole word"""
    word = get_words()
    print("\nA word has been selected")
    print(f"The word contains {len(word)} letters")
    print(word)

    while guess == False:
        letter = input("\nGuess a letter:").lower()
        if letter == word:
            print("you guessed the word")
            guess == True
        elif letter in word:
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
    get_words()
    start_game() 


main()




