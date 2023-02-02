# Write a program that reads usernames on a single line (separated by ", ") and
# prints all valid usernames on separate lines.
# A valid username:
# •	has length between 3 and 16 characters inclusive
# •	can contain only letters, numbers, hyphens, and underscores
# •	has no redundant symbols before, after, or in between

import re


def is_length_valid(name: str) -> bool:
    if 3 <= len(name) <= 16:
        return True
    return False


def are_chars_valid(name: str) -> bool:
    if re.match('[-0-9a-zA-Z_]+$', name):
        return True
    return False


def no_redundancies(name: str) -> bool:
    if ' ' in name:
        return False
    return True


def main():
    usernames = input().split(', ')
    for username in usernames:
        if is_length_valid(username) and are_chars_valid(username) and no_redundancies(username):
            print(username)


if __name__ == '__main__':
    main()
