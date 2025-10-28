"""
Simple Hangman game (single file).
Save as hangman.py and run: python hangman.py
"""

import random
import string
import sys

HANGMAN_PICS = [
r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""
]

WORD_LIST = [
    "python","hangman","computer","programming","development","function",
    "variable","syntax","keyboard","internet","condition","loop","string",
    "module","package","repository","algorithm","binary","debugging",
    "exception","process","thread","resource","network","compiler"
]

def choose_word(words):
    return random.choice(words).lower()

def display_state(secret, guesses):
    shown = " ".join([c if c in guesses else "_" for c in secret])
    return shown

def wrong_guesses_count(secret, guesses):
    wrong = [g for g in guesses if g not in secret]
    return len(wrong)

def get_input_letter(already_guessed):
    while True:
        s = input("Guess a letter (or type a full-word guess): ").strip().lower()
        if not s:
            print("Please enter something.")
            continue
        # full-word guess (length > 1)
        if len(s) > 1:
            if all(ch in string.ascii_lowercase for ch in s):
                return s
            else:
                print("Only alphabetic characters please.")
                continue
        # single-letter guess
        if s in already_guessed:
            print(f"You already guessed '{s}'. Try again.")
            continue
        if s not in string.ascii_lowercase:
            print("Please enter a letter (a-z).")
            continue
        return s

def play_round(words, max_wrong=None):
    secret = choose_word(words)
    guesses = set()
    if max_wrong is None:
        max_wrong = len(HANGMAN_PICS) - 1

    while True:
        wrong_count = wrong_guesses_count(secret, guesses)
        print(HANGMAN_PICS[min(wrong_count, len(HANGMAN_PICS) - 1)])
        
        print("Word: ", display_state(secret, guesses))
        print(f"Incorrect guesses: {wrong_count}/{max_wrong}")
        print("Guessed letters:", " ".join(sorted(g for g in guesses if len(g)==1)))

        guess = get_input_letter(guesses)

        # full-word guess
        if len(guess) > 1:
            if guess == secret:
                print(f"Nice! You correctly guessed the word: {secret}")
                return True
            else:
                print(f"'{guess}' is not the word.")
                # count as one wrong guess
                guesses.add(guess)  # treat full-word wrong guesses in wrong list
        else:
            guesses.add(guess)
            if all(c in guesses for c in secret):
                print(" ".join(secret))
                print(f"Congratulations — you found the word: {secret}")
                return True

        wrong_count = wrong_guesses_count(secret, guesses)
        if wrong_count >= max_wrong:
            print(HANGMAN_PICS[wrong_count])
            print(f"You lost. The word was: {secret}")
            return False

def choose_difficulty():
    print("Select difficulty:")
    print("1) Easy   (7 wrong guesses allowed)")
    print("2) Medium (5 wrong guesses allowed)")
    print("3) Hard   (3 wrong guesses allowed)")
    while True:
        c = input("Choose 1/2/3 (default 1): ").strip() or "1"
        if c in ("1","2","3"):
            return {"1":7, "2":5, "3":3}[c]
        print("Invalid choice.")

def main():
    print("Welcome to Hangman!")
    max_wrong = choose_difficulty()
    words = WORD_LIST[:]  # you could extend or load your own
    wins = 0
    losses = 0

    try:
        while True:
            won = play_round(words, max_wrong=max_wrong)
            if won: wins += 1
            else: losses += 1
            print(f"Score: {wins} wins, {losses} losses")
            again = input("Play again? (y/N): ").strip().lower()
            if again != "y":
                print("Thanks for playing — goodbye!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\nExiting. Bye!")
        sys.exit(0)

if __name__ == "__main__":
    main()
