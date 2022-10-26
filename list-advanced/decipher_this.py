# You are given a secret message you should decipher. To do that, you need to know that in each word:
# •	the second and the last letter are switched (e.g., Holle means Hello)
# •	the first letter is replaced by its character code (e.g., 72 means H)

ciphered_word = input().split(' ')
deciphered_message = []

for word in ciphered_word:
    numbers = [digit for digit in word if digit.isdigit()]
    first_letter = chr(int(''.join(numbers)))
    wrd = [letter for letter in word if letter.isalpha()]
    wrd.insert(0, first_letter)
    wrd[1], wrd[-1] = wrd[-1], wrd[1]
    secret_word = ''.join(wrd)
    deciphered_message.append(secret_word)

print(*deciphered_message, sep=' ')
