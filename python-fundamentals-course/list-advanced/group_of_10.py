# Write a program that receives a sequence of numbers (a string containing integers separated by ", ") and
# prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
# Examples:
# •	The numbers 2, 8, 4, and 10 fall into the group of 10's.
# •	The numbers 13, 19, 14, and 15 fall into the group of 20's.
# For more clarification, see the examples below.

from math import ceil

numbers = [int(num) for num in input(). split(', ')]
max_group = ceil(max(numbers) / 10)

for group in range(1, max_group + 1):
    numbers_copy = numbers.copy()
    current_group = []
    group_by_ten = group * 10
    for num in numbers_copy:
        if num <= group_by_ten:
            current_group.append(num)
            numbers.remove(num)
    print(f"Group of {group_by_ten}'s: {current_group}")
