# Write a program that receives a list of integer numbers (separated by a single space) and a number n.
# The number n represents the count of numbers to remove from the list. You should remove the smallest ones, and then,
# you should print all the numbers that are left in the list, separated by a comma and a space ", ".

list_of_numbers = input().split(' ')
numbers_to_remove = int(input())
str_to_int_list = []

for number in list_of_numbers:
    str_to_int_list.append(int(number))
list_of_numbers = str_to_int_list

for number in range(numbers_to_remove):
    list_of_numbers.remove(min(list_of_numbers))

print(*list_of_numbers, sep=', ')
