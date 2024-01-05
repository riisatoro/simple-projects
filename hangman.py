"""
Simple hangman game.
Guess the word by guessing letters one by one before you run out of guesses.
"""
import random


WORDS = [
    'apple', 'secret', 'python', 'programming', 'hangman', 'code', 'computer', 'banana',
]


def get_random_word():
    """Return a random word from the list of available words."""
    random.shuffle(WORDS)
    return random.choice(WORDS)


def make_word_to_print(word, guessed_letters):
    """Print the word with underscores for letters not guessed."""
    return ''.join((letter if letter in guessed_letters else "_") for letter in word)


def check_win_or_loose(word, print_word, guesses_left):
    if '_' not in print_word:
        return f"You win! The word was: {word}"
    elif guesses_left == 0:
        return f"You lose! The word was: {word}"
    return False


def main():
    """Main function."""
    word = get_random_word()
    guessed_letters = set()
    guesses_left = 8

    print(f"Welcome to Hangman! You have {guesses_left} guesses to guess the word.")
    while True:
        print_word = make_word_to_print(word, guessed_letters)
        win_or_loose = check_win_or_loose(word, print_word, guesses_left)
        if win_or_loose:
            print(win_or_loose)
            break

        print(f"You have {guesses_left} guesses left.")
        print(f"Word: {print_word}")
        letter = input("Guess a letter: ")

        if letter in guessed_letters:
            print("You already guessed that letter!")
            continue

        if letter in word:
            guessed_letters.add(letter)
        else:
            guesses_left -= 1


if __name__ == '__main__':
    main()

