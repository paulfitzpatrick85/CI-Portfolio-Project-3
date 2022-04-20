import random
"""import random"""


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


def play_again():
    print("Would you like to play again?")
    play_again = input("\ny/n?").lower()
    if play_again == "y":
        start_game()
    elif play_again == "n":
        print("\nOkay, we'll return to start & begin when ready")
        main()


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


def start_game():
    """starts game by first selecting random word from list,
    then asks user to guess letter or whole word"""
    guess = False
    guesses_left = 4
    word = get_words()
    print("\nA word has been selected")
    print(f"The word contains {len(word)} letters")
    print(word)

    wrong_guesses = ["wrong guesses:"]
    #hangman_acsii = []

    while guess is False:
        letter = input("\nGuess a letter:").lower()
        if letter.isalpha() is True:
            if letter == word:
                print("You guessed the word!!")
                guess = True
                play_again()
           
            elif letter in word:
                print(f"'{letter}' is in there!")
                position = word.find(letter)
                if position == 0:
                    print(letter, "_ _ _ ")
                if position == 1:
                    print("_", letter, "_ _  ")
                if position == 2:
                    print("_ _", letter, "_ ")
                if position == 3:
                    print("_ _ _", letter)

            elif letter not in word:
                print(f"Sorry, '{letter}' is not in the word!")
                guesses_left -= 1
                wrong_guesses.append(letter)
                print(f"guesses left {guesses_left}")
                print(wrong_guesses) 
                if guesses_left == 0:
                    print("GAME OVER!!")
                    print("You've ran out of guesses!")
                    play_again()
                   
        else:
            print("input letters only")


def main():
    """Main function to hold all functions"""
    welcome_message()
    initiate_game()
    get_words()
    start_game() 
    play_again()


main()




