import random

word_bank = ["rocket", "python", "planet", "laptop", "ocean"]
secret_word = random.choice(word_bank)

guessed = set()
attempts_left = 6

print("=== Welcome to Mystery Word Game ===")

while attempts_left > 0:
    current = ""

    for ch in secret_word:
        if ch in guessed:
            current += ch + " "
        else:
            current += "_ "

    print("\nWord:", current)

    if "_" not in current:
        print("Excellent! You discovered the word:", secret_word)
        break

    letter = input("Guess one letter: ").lower()

    if len(letter) != 1 or not letter.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    if letter in guessed:
        print("Letter already tried.")
        continue

    guessed.add(letter)

    if letter not in secret_word:
        attempts_left -= 1
        print("Incorrect! Attempts left:", attempts_left)
else:
    print("Out of attempts. The word was:", secret_word)