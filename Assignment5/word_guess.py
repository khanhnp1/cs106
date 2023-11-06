"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    """
    Add your code (remember to delete the "pass" below)
    """
    guess_left = INITIAL_GUESSES
    letter_left = len(secret_word)
    guess_str = "-" * letter_left

    while (guess_left > 0):
        print("The word now looks like this: ", guess_str)
        print("You have", guess_left, "guesses left")
        guess_letter = input("Type a single letter here, then press enter: ")
        guess_letter = guess_letter.upper()
        is_correct = 0

        if len(guess_letter) > 1:
            print("Guess should only be a single character")
            continue
        
        for i in range (len(secret_word)):
            if secret_word[i] == guess_letter:
                is_correct = 1
                if guess_str[i] == '-':
                    letter_left -= 1
                    guess_str = guess_str[:i] + guess_letter + guess_str[i + 1:]
        
        if (is_correct == 0):
            guess_left -= 1
            print("There are no", guess_letter,"'s in the word")
        else:
            print("That guess is correct.")
        
        if (letter_left == 0):
            print("Congratulations, the word is:", guess_str)
            break
                
    if (guess_left == 0):
        print("Sorry, you lost. The secret word was: ", secret_word)
    
    return



def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    secret_word = ""
    index = random.randint(1, 121757)
    with open (LEXICON_FILE) as fp:
        for count, line in enumerate(fp):
            if count == index:
                secret_word = line.strip()

    return secret_word


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()