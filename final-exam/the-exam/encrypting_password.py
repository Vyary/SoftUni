import re

number_of_passwords = int(input())

for _ in range(number_of_passwords):
    test_passwords = input()
    pattern = r"(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1+"
    match = re.search(pattern, test_passwords)
    if match:
        encrypted_password = (
            match.group(2) + match.group(3) + match.group(4) + match.group(5)
        )
        print(f"Password: {encrypted_password}")
    else:
        print("Try another password!")
