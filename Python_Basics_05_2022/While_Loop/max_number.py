import sys

max_number = - sys.maxsize
current_input = input()

while current_input != 'Stop':
    current_input = int(current_input)
    if current_input > max_number:
        max_number = current_input
    current_input = input()

print(max_number)
