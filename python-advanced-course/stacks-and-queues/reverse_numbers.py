stack_of_numbers = input().split()

for _ in range(len(stack_of_numbers)):
    print(stack_of_numbers.pop(), end=" ")


"""                     Task:
Write a program that reads a string with N integers from the console,
separated by a single space, and reverses them using a stack.
Print the reversed integers on one line, separated by a single space.

Example:
Input:
1 2 3 4 5
Output:
5 4 3 2 1
"""
