import random

word_list = ['banana', 'mango', 'lychee', 'strawberry', 'grapes']

print(word_list)

word = random.choice(word_list)

print(word)

guess = input("Enter a single letter: ")

if len(guess) == 1 and guess.isalpha():
    print ("Good Guess!")
else:
    print ("Oops! That is not a valid input.")
