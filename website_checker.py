"""
Checks the website availability from the list of websites in .csv file
"""
import csv
import os
from http import HTTPStatus

import requests
from fake_useragent import UserAgent


def get_websites(csv_path: str) -> list[str]:
    websites: list[str] = []
    file_path = os.path.join('sources', csv_path)
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if 'https://' not in row[1] and 'http://' not in row[1]:
                websites.append(f'https://{row[1]}')
            else:
                websites.append(row[1])
    return websites


def get_user_agent() -> str:
    return UserAgent().random


def get_status_description(status_code: int) -> str:
    try:
        phrase = HTTPStatus(status_code).phrase
    except ValueError:
        phrase = 'Unknown status'
    return f"({status_code}: {phrase})"


def check_website(website: str, user_agent) -> None:
    try:
        response = requests.get(website, headers={'User-Agent': user_agent})
        print(f'{website} - {get_status_description(response.status_code)}')
    except Exception as e:
        print(f'Could not get info from the {website} - {e}')


def main():
    websites: list[str] = get_websites('websites.csv')
    user_agent: str = get_user_agent()
    for website in websites:
        check_website(website, user_agent)


if __name__ == '__main__':
    main()
