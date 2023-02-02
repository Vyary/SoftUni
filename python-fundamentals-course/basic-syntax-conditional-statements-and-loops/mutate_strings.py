# You will be given two strings. Transform the first string into the second one,
# letter by letter, starting from the first one. After each interaction,
# print the resulting string only if it is unique.
# Note: the strings will have the same length.

word_one = input()
word_two = input()
previous_word = word_one

for letter in range(len(word_one)):
    new_word = ''
    new_word += word_two[:letter + 1]
    new_word += word_one[letter + 1:]
    if new_word == previous_word:
        continue
    else:
        print(new_word)
    previous_word = new_word
