"""
Play the game:
    1. Create answer + initialize Guesses
    2. Prompt user for a guess, initialize WordleString + add to Guesses
    3. Print the status
    4. Limit to 4 guesses
"""
from game_class import WordleString, Guesses
import random
import nltk
from nltk.corpus import words


nltk.download('words')

five_letter_words = [w for w in words.words() if len(w) == 5]
answer = random.choice(five_letter_words).upper()

guesses = Guesses(answer=answer)

for _ in range(6):
    new_guess = input("Guess something queen >>> ")
    if len(new_guess) != 5:
        new_guess = input("Guess something that's 5 letters or more queen >>> ")
    new_wordle_string = WordleString(new_guess.upper())
    guesses.add_guess(new_wordle_string)
    correction_result = guesses.correct(guess=guesses.get_last_guess())
    if correction_result:
        print("YAY DONE")
        break

print(f"Word was {answer}")
