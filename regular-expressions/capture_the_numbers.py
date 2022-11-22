# Write a program that receives strings on different lines and extracts only the numbers.
# Print all extracted numbers on a single line, separated by a single space.

import re

line = input()

while line:
    pattern = r'\d+'
    match = re.findall(pattern, line)
    if match:
        print(' '.join(match), end=' ')
    line = input()
