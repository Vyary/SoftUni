# Write a program that receives a single string containing positive and negative numbers separated by a single space.
# Print a list containing the opposite of each number.

input_string = input()

separate_string_list = input_string.split(' ')
reversed_list = []

for number in separate_string_list:
    reversed_number = -int(number)
    reversed_list.append(reversed_number)

print(reversed_list)
