"""Datheon Internship Task 1: Hangman Word Guessing Game."""

import random
from pathlib import Path


WORD_LIST_FILE = Path(__file__).with_name("google-10000-english-no-swears.txt")
MAX_WRONG_GUESSES = 6

HANGMAN_STAGES = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """,
]


def load_words():
    """Load suitable words from the provided Datheon text file."""
    try:
        with WORD_LIST_FILE.open("r", encoding="utf-8") as file:
            words = [
                line.strip().lower()
                for line in file
                if line.strip().isalpha()
                and line.strip().isascii()
                and 4 <= len(line.strip()) <= 12
            ]
    except OSError:
        print(f"Error: Could not open {WORD_LIST_FILE.name}.")
        print("Keep the word-list TXT file in the same folder as hangman.py.")
        return []

    return words


def display_word(secret_word, guessed_letters):
    """Show guessed letters and underscores for hidden letters."""
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


def play_game():
    words = load_words()
    if not words:
        return

    secret_word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = 0

    print("\nWelcome to Hangman!")
    print("Guess the hidden English word one letter at a time.")
    print(f"You can make {MAX_WRONG_GUESSES} incorrect guesses.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print(HANGMAN_STAGES[wrong_guesses])
        print("Word:", display_word(secret_word, guessed_letters))
        print("Guessed letters:", " ".join(sorted(guessed_letters)) or "None")
        print(f"Wrong guesses: {wrong_guesses}/{MAX_WRONG_GUESSES}")

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word!")
            return

        guess = input("\nGuess one English letter: ").strip().lower()

        if len(guess) != 1 or not guess.isascii() or not guess.isalpha():
            print("Please enter one English letter (A-Z).\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. No penalty.\n")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!\n")
        else:
            wrong_guesses += 1
            print("Wrong guess!\n")

    print(HANGMAN_STAGES[MAX_WRONG_GUESSES])
    print("Game Over! You ran out of attempts.")
    print("The correct word was:", secret_word)


if __name__ == "__main__":
    play_game()
