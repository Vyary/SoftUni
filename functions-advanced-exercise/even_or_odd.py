def even_odd(*args):
    numbers = args[:-1]
    command = args[-1]
    if command == "even":
        result = [num for num in numbers if num % 2 == 0]
    else:
        result = [num for num in numbers if num % 2 == 1]
    return list(result)


"""                     Task:
Create a function called even_odd() that can receive a different quantity of numbers and
a command at the end. The command can be "even" or "odd". Filter the numbers depending
on the command and return them in a list. Submit only the function in the judge system.

Example:
Test Code:
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
Output:
[1, 3, 5, 7, 9]
"""
