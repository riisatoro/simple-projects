def check_password(password: str) -> tuple[int | None, bool]:
    with open('sources/common_passwords.txt', 'r') as file:
        common_passwords: list[str] = file.readlines()

    for index, common_pwd in enumerate(common_passwords, start=1):
        if common_pwd.lower() == password.lower():
            return index, True
    return None, False


def main():
    password: str = input('Enter password: ')
    index, is_common = check_password(password)
    if is_common:
        print(f'Your password is too weak (#{index} in list). Please, change it.')
    else:
        print('Your password is strong enough.')


if __name__ == '__main__':
    main()
