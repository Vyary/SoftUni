# Write a program that receives two numbers (factor and count). It should create a list with
# a length of the given count that contains only integer numbers, which are multiples of the given factor.
# The numbers should be only positive, and they should be arranged in ascending order,
# starting from the value of the factor.

factor = int(input())
count = int(input())
number_list = []

for number in range(1, count + 1):
    multiplied_number = number * factor
    number_list.append(multiplied_number)

print(number_list)
