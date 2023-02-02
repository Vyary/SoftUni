# John invented a game with numbers and letters from the English alphabet. The game was simple.
# You receive a string consisting of a number between two letters. For the given string,
# you should perform different mathematical operations to achieve a result:
# •	First, if the letter in front of the number is:
# o	Uppercase: divide the number by the letter's position in the alphabet (starting from 1)
# o	Lowercase: multiply the number with the letter's position in the alphabet (starting from 1)
# •	Next, if the letter after the number is:
# o	Uppercase: subtract its position from the resulting number (starting from 1)
# o	Lowercase: add its position to the resulting number (starting from 1)
# The game was too easy for John. He decided to complicate it by doing the same calculations to
# multiple strings keeping track of only the total sum of all results.
# Once he started to solve this with more strings and bigger numbers, it became quite hard to do it only in his mind.
# He kindly asks you to write a program that performs the operations described above and
# sums the final results of each string.
# Input
# •	The input comes from the console as a single line, holding a sequence of strings
# •	Strings are separated by one or more white spaces
# •	The input data will always be valid. There is no need to check it explicitly
# Output
# •	Print at the console a single number:
# o	The total sum of all processed numbers, formatted to the second decimal separator

import re

sequence_of_strings = input().split()
total_sum = 0

for string in sequence_of_strings:
    number = int(re.search(r'\d+', string)[0])
    letter_before = string[0]
    letter_after = string[-1]
    letter_before_position = ord(letter_before.lower()) - 96
    letter_after_position = ord(letter_after.lower()) - 96

    if letter_before.isupper():
        number = number / letter_before_position
    elif letter_before.islower():
        number = number * letter_before_position

    if letter_after.isupper():
        number = number - letter_after_position
    elif letter_after.islower():
        number = number + letter_after_position

    total_sum += number

print(f'{total_sum:.2f}')
