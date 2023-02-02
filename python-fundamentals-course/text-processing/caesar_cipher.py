# Write a program that returns an encrypted version of the same text.
# Encrypt the text by replacing each character with
# the corresponding character three positions forward in the ASCII table.
# For example, A would be replaced with D, B would become E, and so on. Print the encrypted text.

start_text = input()
encrypted_text = ''

for char in start_text:
    new_letter = chr(ord(char) + 3)
    encrypted_text += new_letter

print(encrypted_text)

# start_text = input()
# encrypted_text = [chr(ord(letter) + 3) for letter in start_text]
# print(''.join(encrypted_text))
