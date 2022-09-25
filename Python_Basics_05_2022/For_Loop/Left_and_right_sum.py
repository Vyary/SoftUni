number_of_numbers = int(input())
left_side_numbers = 0
right_side_numbers = 0


for number in range(number_of_numbers * 2):
    input_number = int(input())
    if number < number_of_numbers:
        left_side_numbers += input_number
    else:
        right_side_numbers += input_number

if left_side_numbers == right_side_numbers:
    print(f'Yes, sum = {left_side_numbers}')
else:
    diff = abs(left_side_numbers - right_side_numbers)
    print(f'No, diff = {diff}')
