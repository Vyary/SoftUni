# Write a program that finds all variable names in each string. A variable name starts with an underscore ("_") and
# contains only capital and non-capital letters and digits. Extract only their names without the underscore.
# Try to do this only with regular expressions.
# The output consists of all variable names extracted and printed on a single line, separated by a comma.

import re

line = input()
pattern = r'\b\_([A-Za-z0-9]+)\b'
match = re.findall(pattern, line)
print(','.join(match))
