import random
import time

words = ["apple", "banana", "orange", "grapes", "papaya", "mango"]
word = random.choice(words)
guessed = []
missed_guesses = 0
max_attempts = 6

hangman = [
"""
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

print("Welcome to hangman!")
print("Hint: the word is a fruit!")
time.sleep(1)

while missed_guesses < max_attempts:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print(hangman[missed_guesses])
    print("Word:", display)

    if "_" not in display:
        print("Congratulations! You guessed the word!")
        break

    guess = input("Enter your guess: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a letter!")
        continue

    elif guess in guessed:
        print("You already guessed the letter", guess)
        continue

    guessed.append(guess)

    if guess in word:
        print("You guessed the letter", guess)
    else:
        missed_guesses += 1
        print("Wrong guess!")

else:
    time.sleep(1)
    print("Game over!")
    time.sleep(1)
    print("The word was", word)