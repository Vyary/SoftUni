# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"

work_str = input().replace(' ', '')
occurrences_dictionary = {}

for letter in work_str:
    if letter not in occurrences_dictionary.keys():
        occurrences_dictionary[letter] = 0
    occurrences_dictionary[letter] += 1

for char, occurrences in occurrences_dictionary.items():
    print(f"{char} -> {occurrences}")
