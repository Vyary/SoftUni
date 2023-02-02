# Write a program to read a sequence of integers and find and print the top 5 numbers greater than the average value in
# the sequence, sorted in descending order.
# Input
# •	Read from the console a single line holding space-separated integers.
# Output
# •	Print the above-described numbers on a single line, space-separated.
# •	If less than 5 numbers hold the property mentioned above, print less than 5 numbers.
# •	Print "No" if no numbers hold the above property.

numbers = [int(num) for num in input().split(' ')]

average_number = sum(numbers) / len(numbers)
more_than_average_numbers = [num for num in numbers if num > average_number]
reversed_more_than = sorted(more_than_average_numbers, reverse=True)

if len(more_than_average_numbers) < 1:
    print('No')
else:
    print(*reversed_more_than[:5:], sep=' ')
