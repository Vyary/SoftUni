from math import floor

best_word = ''
best_points = 0

word = input()

while word != 'End of words':
    current_points = 0
    for letter in range(len(word)):
        current_points += ord(word[letter]) # ord is used to find ASCII number

    if word[0] == 'A' or word[0] == 'E' or word[0] == 'I' or word[0] == 'O' or word[0] == 'U' or word[0] == 'Y':
        current_points = floor(current_points * len(word))
    elif word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u' or word[0] == 'y':
        current_points = floor(current_points * len(word))
    else:
        current_points = floor(current_points / len(word))

    if current_points > best_points:
        best_word = word
        best_points = current_points

    word = input()

print(f"The most powerful word is {best_word} - {best_points}" )
