# Write a function that checks if a given password is valid. Password validations are:
# •	It should be 6 - 10 (inclusive) characters long
# •	It should consist only of letters and digits
# •	It should have at least 2 digits
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
# •	"Password must be between 6 and 10 characters"
# •	"Password must consist only of letters and digits"
# •	"Password must have at least 2 digits"

def pass_length_checker(password: str) -> bool:
    if 6 <= len(password) <= 10:
        return True
    return False


def letters_and_digits(password: str) -> bool:
    if password.isalnum():
        return True
    return False


def more_than_two_digits(password: str) -> bool:
    digit_count = 0
    for char in password:
        if char.isdigit():
            digit_count += 1
            if digit_count >= 2:
                return True
    return False


input_password = input()
valid_len = pass_length_checker(input_password)
only_letters_and_digits = letters_and_digits(input_password)
has_more_than_two_digits = more_than_two_digits(input_password)

if not valid_len:
    print("Password must be between 6 and 10 characters")
if not only_letters_and_digits:
    print("Password must consist only of letters and digits")
if not has_more_than_two_digits:
    print("Password must have at least 2 digits")
if valid_len and only_letters_and_digits and has_more_than_two_digits:
    print("Password is valid")
