def func_executor(*func_data):
    result = []

    for func, args in func_data:
        result.append(f"{func.__name__} - {func(*args)}")

    return "\n".join(result)


"""                     Task:
Write a concatenate() function that receives some strings as arguments and some named
arguments (the key will be a string, and the value will be another string).
First, you should concatenate all arguments successively. Next, take each key
successively, and if it is present in the resulted string, change all matching parts
with the key's value. In the end, return the final string.
 See the examples for more clarification.

Example:
Test Code:
def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
Output:
sum_numbers - 3
multiply_numbers - 8
"""
