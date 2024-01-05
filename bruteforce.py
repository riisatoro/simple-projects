from datetime import datetime, timedelta
import itertools
import string


def bruteforce(
        control_pwd: str,
        length: int,
        letters: bool = True,
        digits: bool = False,
        punctuation: bool = False,
        uppercase: bool = False,
        stop_iter: int = 10 ** 6
) -> tuple[bool, int, timedelta]:
    """Bruteforce the password until match"""

    if not any([letters, digits, punctuation, uppercase]):
        raise ValueError('At least one of the parameters should be True')

    chars: str = ''
    if letters:
        chars += string.ascii_letters
    if digits:
        chars += string.digits
    if punctuation:
        chars += string.punctuation
    if uppercase:
        chars += string.ascii_uppercase

    start_time = datetime.now()
    iterators = itertools.product(chars, repeat=length)

    for i in range(stop_iter):
        password = ''.join(next(iterators))
        if password == control_pwd:
            gen_time: timedelta = datetime.now() - start_time
            return True, i, gen_time

    gen_time: timedelta = datetime.now() - start_time
    return False, stop_iter, gen_time


def get_user_input(
        message: str,
        allow_none: bool = False,
        choices: list[str] = [],
) -> str | None:
    user_input: str | int | None = input(message)
    while True:
        if user_input and choices and user_input.lower() not in choices:
            user_input = input(f"Not a valid input choice. {message}")
        elif not user_input and not allow_none:
            user_input = input(f"Not a valid input. {message}")
        else:
            return user_input


def main():
    control_pwd: str = get_user_input("Enter password to crack: ")
    raw_iterations: int | str | None = get_user_input(
        "Enter number of iterations (leave empty for default: 10^6): ",
        allow_none=True
    )
    iteration = int(raw_iterations) if raw_iterations else 10 ** 6

    raw_has_letters: str | None = get_user_input(
        "Should the password contain letters? (y/n): ",
        choices=['y', 'n']
    )
    has_letters = True if raw_has_letters == 'y' else False

    raw_has_digits: str | None = get_user_input(
        "Should the password contain digits? (y/n): ",
        choices=['y', 'n']
    )
    has_digits = True if raw_has_digits == 'y' else False

    raw_has_uppercase: str | None = get_user_input(
        "Should the password contain uppercase? (y/n): ",
        choices=['y', 'n']
    )
    has_uppercase = True if raw_has_uppercase == 'y' else False

    raw_has_punctuation: str | None = get_user_input(
        "Should the password contain punctuation? (y/n): ",
        choices=['y', 'n']
    )
    has_punctuation = True if raw_has_punctuation == 'y' else False

    length: int = len(control_pwd)
    cracked, iterations, gen_time = bruteforce(
        control_pwd, length, has_letters, has_digits, has_punctuation, has_uppercase, iteration
    )
    if cracked:
        print(f'Password was cracked in {iterations} iterations and {gen_time} time was spent.')
    else:
        print(f'Password was not cracked in {iterations}')


if __name__ == '__main__':
    main()
