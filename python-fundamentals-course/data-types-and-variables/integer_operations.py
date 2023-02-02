# Write a program that reads four integer numbers. It should add the first to the second number,
# integer divide the sum by the third number, and multiply the result by the fourth number.
# Print the final result.
from math import floor

first_number = int(input())
second_number = int(input())
third_number = int(input())
forth_number = int(input())

total = int((first_number + second_number) / third_number) * forth_number

print(total)
