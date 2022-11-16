# Write a program that reads a string from the console and replaces any sequence of
# the same letters with a single corresponding letter.

text = input()
previous_letter = ''
final_text = ''

for letter in text:
    if letter != previous_letter:
        previous_letter = letter
        final_text += letter

print(final_text)
