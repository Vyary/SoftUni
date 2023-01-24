stack = []

number_of_lines = int(input())

command_dict = {
    1: lambda command: stack.append(command[1]),
    2: lambda command: stack.pop() if stack else None,
    3: lambda command: print(max(stack)) if stack else None,
    4: lambda command: print(min(stack)) if stack else None,
}

for line in range(number_of_lines):
    command = [int(x) for x in input().split()]
    command_dict[command[0]](command)

print(", ".join(str(stack.pop()) for _ in range(len(stack))))


"""                     Task:
You have an empty stack. You will receive an integer - N. On the next N lines,
you will receive queries. Each query is one of these four types:
•	'1 {number}' - push the number (integer) into the stack
•	'2' - delete the number at the top of the stack
•	'3' - print the maximum number in the stack
•	'4' - print the minimum number in the stack
It is guaranteed that each query is valid.
After you go through all the queries, print the stack from top to bottom in
the following format:
"{n}, {n1}, {n2}, ... {nn}"

Example:
Input:
9
1 97
2
1 20
2
1 26
1 20
3
1 91
4
Output:
26
20
91, 20, 26
"""
