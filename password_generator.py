"""
Secure password generator function.

Creates a password of length n, with at least one uppercase letter, one lowercase letter, one number, and one special character.
Containing of special symbols are customizable.
"""
import string
import secrets


def contains_uppercase(password: str) -> bool:
    return any(c.isupper() for c in password)


def contains_punctuation(password: str) -> bool:
    return any(c in string.punctuation for c in password)


def password_generator(length: int, symbols: bool, uppercase: bool) -> str:
    combinations = string.ascii_lowercase + string.digits
    if symbols:
        combinations += string.punctuation
    if uppercase:
        combinations += string.ascii_uppercase

    combination_length = len(combinations)
    new_password = ""
    for _ in range(length):
        new_password += combinations[secrets.randbelow(combination_length)]

    return new_password


def input_user_configuration():
    length = int(input("How long should the password be? >> "))
    symbols = input("Should the password contain special characters? (y/n) >> ").lower() == "y"
    uppercase = input("Should the password contain uppercase letters? (y/n) >> ").lower() == "y"
    return length, symbols, uppercase


if __name__ == "__main__":
    length, symbols, uppercase = input_user_configuration()

    new_pwd = password_generator(length, symbols, uppercase)
    while contains_uppercase(new_pwd) != uppercase or contains_punctuation(new_pwd) != symbols:
        new_pwd = password_generator(length, symbols, uppercase)

    result: str = f"U:{contains_uppercase(new_pwd)} S:{contains_punctuation(new_pwd)}\nPWD: {new_pwd}"
    print(result)
