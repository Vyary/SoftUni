# You will receive three integer numbers.
# Write functions named:
# •	sum_numbers() that returns the sum of the first two integers
# •	subtract() that returns the difference between the returned result of the first function and the third integer
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
# Print the result of subtract() function on the console.

def add_and_subtract(number1: int, number2: int, number3: int) -> int:
    def sum_numbers(first_number: int, second_number: int) -> int:
        return first_number + second_number

    def subtract(sum_of_numbers: int, third_number: int) -> int:
        return sum_of_numbers - third_number

    sum_number = sum_numbers(number1, number2)
    result = subtract(sum_number, number3)
    return result


print(add_and_subtract(int(input()), int(input()), int(input())))
