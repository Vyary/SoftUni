import sys

min_number = sys.maxsize
current_input = input()

while current_input != 'Stop':
    current_input = int(current_input)
    if current_input < min_number:
        min_number = current_input
    current_input = input()

print(min_number)
