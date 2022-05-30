number_of_numbers = int(input())
even_number_result = 0
odd_number_result = 0

for number in range(number_of_numbers):
    current_number = int(input())
    if number % 2 == 0:
        even_number_result += current_number
    else:
        odd_number_result += current_number

if even_number_result == odd_number_result:
    print('Yes')
    print(f'Sum = {even_number_result}')
else:
    print('No')
    diff = abs(even_number_result - odd_number_result)
    print(f'Diff = {diff}')
