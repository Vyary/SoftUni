start_number = int(input())
end_number = int(input())
magic_number = int(input())
total_combinations = 0
first_magic_combination = 0

for number_one in range(start_number, end_number + 1):
    for number_two in range(start_number, end_number + 1):
        total_combinations += 1
        if number_one + number_two == magic_number and first_magic_combination == 0:
            first_magic_combination = total_combinations
            first_magic_number = number_one
            second_magic_number = number_two

if first_magic_combination != 0:
    print(f"Combination N:{first_magic_combination} ({first_magic_number} + {second_magic_number} = {magic_number})")
else:
    print(f"{total_combinations} combinations - neither equals {magic_number}")
