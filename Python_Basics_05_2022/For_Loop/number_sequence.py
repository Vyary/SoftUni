import sys

number_of_numbers = int(input())
max_num = - sys.maxsize
min_num = sys.maxsize

for number in range(number_of_numbers):
    level = int(input())
    if level > max_num:
        max_num = level
    if level < min_num:
        min_num = level

print(f'Max number: {max_num}')
print(f'Min number: {min_num}')
