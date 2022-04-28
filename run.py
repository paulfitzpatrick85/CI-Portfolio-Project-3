import random
"""import random"""


def welcome_message():
    """Welcome user to game upon loading"""
    print("""   -------------------------------------------------\n
     *********** Welcome to HangMan! ************\n
     The program will select a word at random.
     Your job is to guess, one letter at a time,
     what that word is.
     With each incorrect answer the hangman will
     appear one body part at a time.
     You are allowed six wrong guesses.
                      Good Luck!
     \n   -------------------------------------------------""")


def play_again():
    """ask player if they want to play again once previous game is finished"""
    print("Would you like to play again?")
    while True:
        try:
            p_again = input("\nType 'y' for yes or 'n' for no\n").lower()
            if p_again == "y":
                start_game()
            elif p_again == "n":
                print("\nOkay, we'll return to start & begin when ready")
                main()
            else:
                raise ValueError()
        except ValueError:
            print("You need to type either y or n")


def initiate_game():
    """initiate game after welcome message"""
    while True:
        try:
            name = input("Input your name:\n").lower().capitalize()
            if name.isalpha() is True:
                break
            else:
                raise TypeError()
        except TypeError:
            print("Your name must consist of letters only")
    
    print(f"\n{name}, would you like to play a new game?")

    while True:
        try:
            start_game_question = input("Type 'y'/'n' for yes/no.\n").lower()
            if start_game_question == "y":
                print(f"\nGreat {name}, lets begin!")
                break
            elif start_game_question == "n":
                print(f"\nOkay {name}, we'll return to begin when ready")
                main()
            else:
                raise ValueError()
        except ValueError:
            print("You need to type either y or n")

                
def get_words():
    """collection of words to be used in game"""
    words = ["bake", "word", "list", "four", "five", "best",
             "cute", "zero", "huge", "race", "rice", "lace", "beam"]
    return random.choice(words).lower()


def start_game():
    """starts game by first selecting random word from list,
    then asks user to guess letter or whole word"""
    guess = False
    guesses_left = 6
    word = get_words()
    pos_list = ['_' for x in range(len(word))]
    print("\nA word has been selected")
    print(f"The word contains {len(word)} letters")

    wrong_guesses = ["wrong guesses:"]
    correct_guesses = []
    sorted_word = sorted(word)
    single_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                      "j", "k", "l", "m", "n", "o", "p", "q", "r",
                      "s", "t", "u", "v", "w", "x", "y", "z"]
    # hangman ascii art
    hangman = ["""
  +---+
  |   |
      |
      |
      |
      |
=========""", """  +---+
  |   |
  O   |
      |
      |
      |
=========""", """  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """  +---+
  |   |
  O   |
  |\  |
      |
      |
=========""", """  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """ +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]

    while guess is False:
        letter = input("\nGuess a letter:\n").lower()
        if letter.isalpha() is True:
            if letter == word:
                print("You guessed the word!!")
                guess = True
                play_again()
# deal with input when more than one letter
            elif letter not in single_letters:
                print("\nGuess must be either a single letter or correct word")
                print("and unfortunately that classes as an attempt!")
                guesses_left -= 1
                wrong_guesses.append(letter)
                print(f"guesses left = {guesses_left}")
                if guesses_left == 5:
                    print(hangman[0])
                    print(wrong_guesses)
                elif guesses_left == 4:
                    print(hangman[1])
                    print(wrong_guesses)
                elif guesses_left == 3:
                    print(hangman[2])
                    print(wrong_guesses)
                elif guesses_left == 2:
                    print(hangman[3])
                    print(wrong_guesses)
                elif guesses_left == 1:
                    print(hangman[4])
                    print(wrong_guesses)
                if guesses_left == 0:
                    print("\nGAME OVER!!")
                    print("You've ran out of guesses!")
                    print(hangman[5])
                    play_again()
           
            elif letter in word:
                print(f"\n'{letter}' is in there!")
                correct_guesses.append(letter)
                position = word.find(letter)
                pos_list[position] = letter
                print(' '.join(pos_list))
            
                if sorted_word == sorted(correct_guesses):
                    print("You guessed the word!!")
                    play_again()
                     
            elif letter not in word:
                print(f"\nSorry, '{letter}' is not in the word!")
                guesses_left -= 1
                wrong_guesses.append(letter)
                print(f"guesses left = {guesses_left}")
                if guesses_left == 5:
                    print(hangman[0])
                    print(wrong_guesses)
                elif guesses_left == 4:
                    print(hangman[1])
                    print(wrong_guesses)
                elif guesses_left == 3:
                    print(hangman[2])
                    print(wrong_guesses)
                elif guesses_left == 2:
                    print(hangman[3])
                    print(wrong_guesses)
                elif guesses_left == 1:
                    print(hangman[4])
                    print(wrong_guesses)
                if guesses_left == 0:
                    print("\nGAME OVER!!")
                    print("You've ran out of guesses!")
                    print(hangman[5])
                    play_again()
       
        else:
            print("You can only input letters")


def main():
    """Main function to hold all functions"""
    welcome_message()
    initiate_game()
    get_words()
    start_game()
    play_again()


main()




