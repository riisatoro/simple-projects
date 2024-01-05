"""
This is a number guessing game. The computer will generate a random number, and the user will try to guess it.
"""
import random


def generate_random_number(min_num: int, max_num: int):
    """
    This function generates a random number between the min and max values.
    :param min_num: The minimum value for the random number.
    :param max_num: The maximum value for the random number.
    :return: The random number.
    """
    return random.randint(min_num, max_num)


def get_input_number():
    """
    This function gets the user's input number.
    :return: The user's input number.
    """
    while True:
        try:
            user_input = int(input("Guess a number: "))
            return user_input
        except ValueError:
            print("Please enter a valid number.")


def main():
    guess_limit = 7
    min_num, max_num = 1, 100
    random_number = generate_random_number(min_num, max_num)

    print(f"Welcome to the number guessing game! You have {guess_limit} guesses to guess the number.")
    print(f"The number is between {min_num} and {max_num}.")

    while True:
        if guess_limit == 0:
            print("You ran out of guesses. You lose.")
            print(f"The number was {random_number}.")
            break

        guess = get_input_number()
        if guess == random_number:
            print("You guessed the number!")
            break
        elif guess < random_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        guess_limit -= 1


if __name__ == "__main__":
    main()
