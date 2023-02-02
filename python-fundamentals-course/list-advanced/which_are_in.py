# You will be given two sequences of strings, separated by ", ".
# Print a new list containing only the strings from the first input line,
# which are substrings of any string in the second input line.

first_sequence = input().split(', ')
second_sequence = input().split(', ')
substrings = []

for word1 in first_sequence:
    for word2 in second_sequence:
        if word1 in word2:
            substrings.append(word1)
            break

print(substrings)
