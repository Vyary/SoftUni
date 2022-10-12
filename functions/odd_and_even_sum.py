# You will receive a single number. You should write a function that returns the sum of all even and
# all odd digits in a given number. The result should be returned as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.

def odd_and_even_sum(number: int) -> tuple[int, int]:
    odd_sum = 0
    even_sum = 0
    str_number = str(number)
    for digit in str_number:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return odd_sum, even_sum


input_number = int(input())
odd_sum_total, even_sum_total = odd_and_even_sum(input_number)
print(f"Odd sum = {odd_sum_total}, Even sum = {even_sum_total}")
