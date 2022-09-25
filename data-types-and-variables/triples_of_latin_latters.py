# Write a program to read an integer N and print all triples of the first N small Latin letters,
# ordered alphabetically:

number_of_letters = int(input())

for first_counter in range(number_of_letters):
    first_letter = chr(97 + first_counter)
    for second_counter in range(number_of_letters):
        second_letter = chr(97 + second_counter)
        for third_counter in range(number_of_letters):
            third_letter = chr(97 + third_counter)
            print(f'{first_letter}{second_letter}{third_letter}')
