start_list = input().split("|")

sub_lists = []

for sub_string in start_list[::-1]:
    sub_lists.extend(sub_string.split())

print(*sub_lists)


"""                     Task:
Write a program to flatten several lists of numbers received in the following format:
	String with numbers or empty strings separated by "|"
	Values are separated by spaces (" ", one or several)
	Order the output list from the last to the first matrix sub-lists and their values
from left to right as shown below

Example:
Input:
1 2 3 |4 5 6 |  7  88
Output:
7 88 4 5 6 1 2 3
"""
