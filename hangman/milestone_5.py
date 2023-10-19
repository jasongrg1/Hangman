import random

class Hangman:
    def __init__(self, word_list, num_lives=5):

        self.word = random.choice(word_list)
        self.word_guessed = []
        for i in range(len(self.word)):
            self.word_guessed.append("_")
        
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        
    
    def check_guess(self, guess):
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
        while True:
            guess = input("Enter a single letter: ")
            if not len(guess) == 1 and guess.isalpha():
                print ("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break



def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        print(f"\n Mystery word: \n {game.word_guessed}          Lives: {game.num_lives} \n")
        if game.num_lives == 0:
            print("You lost!")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives != 0 and not game.num_letters > 0:
            print('Congratulations. You won the game!')
            break


fruit_list = ['banana', 'mango', 'lychee', 'strawberry', 'grapes']
play_game(fruit_list)


