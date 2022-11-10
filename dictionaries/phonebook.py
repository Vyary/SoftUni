# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-".
# If you receive a name that already exists in the phonebook, update its number.
# After filling the phonebook, you will receive a number – N.
# Your program should be able to perform a search of contact by name and print its details in the format:
# "{name} -> {number}". In case the contact isn't found, print: "Contact {name} does not exist."

phonebook = {}

while True:
    entry = input().split('-')
    if entry[0].isdigit():
        numbers_to_check = int(entry[0])
        break
    name = entry[0]
    number = entry[1]
    if name not in phonebook:
        phonebook[name] = ''
    phonebook[name] = number

for number in range(int(entry[0])):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
