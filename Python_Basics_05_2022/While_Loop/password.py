name = input()
password = input()
password_try = input()

while password_try != password:
    password_try = input()

print(f'Welcome {name}!')
