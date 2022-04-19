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
        print(f"Okay {name}, we'll return to the start to begin when ready")
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

    while guess is False:
        letter = input("\nGuess a letter:").lower()
        if letter.isalpha() is True:

            if letter == word:
                print("You guessed the word!!")
                guess is True
                print("Would you like to play again?")
                play_again = input("\ny/n?").lower()
                if play_again == "y":
                    start_game()
                elif play_again == "n":
                    print("\nOkay, we'll return to start & begin when ready")
                    main()

            elif letter in word:
                print(f"'{letter}' is in there!")
            #print(f"{letter}")
            else:
                print(f"'{letter}' ain't there sorry!")
        else:
            print("input letters only")


def main():
    """Main function to hold all functions"""
    welcome_message()
    initiate_game()
    get_words()
    start_game() 


main()




