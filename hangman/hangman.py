import random


class Hangman:
    """
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.   
    """

    def __init__(self, word_list, num_lives=5):

        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        """
        Checks if the letter guessed is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        guess: str
            The letter to be checked
        """

        guess = guess.lower()
        if guess in self.word:
            print (f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if guess == self.word[i]:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
            
        else:
            self.num_lives -= 1
            print (f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        """

        while True:
            guess = input("Enter a single letter: ")
            if not (len(guess) == 1 and guess.isalpha()):
                print ("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


def play_game(word_list):
    """
    Initialises a Hangman game.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    """

    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        print(f"\n Mystery word: \n {game.word_guessed} \t\t Lives: {game.num_lives} \n")
        if game.num_lives == 0:
            print(f"You lost! The word was {game.word}")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives != 0 and not game.num_letters > 0:
            print("Congratulations! You won the game!")
            break


if __name__ == '__main__':
    word_list = ['banana', 'mango', 'lychee', 'strawberry', 'grapes']
    play_game(word_list)

