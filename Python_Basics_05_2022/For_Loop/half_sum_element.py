import sys

number_of_numbers = int(input())
max_number = - sys.maxsize
total_numer = 0

for number in range(number_of_numbers):
    current_number = int(input())
    total_numer += current_number
    if current_number > max_number:
        max_number = current_number

total_numer -= max_number

if total_numer == max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    print('No')
    diff = abs(total_numer - max_number)
    print(f'Diff = {diff}')
