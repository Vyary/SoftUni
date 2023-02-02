# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.

def factorial(number: int) -> int:
    total = 1
    for fact in range(1, number + 1):
        total = total * fact
    return total


first_number = int(input())
second_number = int(input())
first_number_factorial = factorial(first_number)
second_number_factorial = factorial(second_number)
final_result = first_number_factorial / second_number_factorial
print(f"{final_result:.2f}")

# print(f'{factorial(int(input())) / factorial(int(input())):.2f}')
