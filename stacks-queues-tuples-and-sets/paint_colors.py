from collections import deque
from math import ceil

color_pieces = deque(input().split())

colors = ["red", "yellow", "blue", "orange", "purple", "green"]
colors_found = []

while color_pieces:

    left_part = color_pieces.popleft()
    right_part = color_pieces.pop() if color_pieces else ""

    if left_part + right_part in colors:
        colors_found.append(left_part + right_part)
        continue
    elif right_part + left_part in colors:
        colors_found.append(right_part + left_part)
        continue

    index = ceil(len(color_pieces) / 2)
    new_left = left_part[:-1]
    new_right = right_part[:-1]

    if new_left:
        color_pieces.insert(index, new_left)
    if new_right:
        color_pieces.insert(index, new_right)

for color in colors_found:
    if color == "orange":
        if "red" not in colors_found or "yellow" not in colors_found:
            colors_found.remove(color)
    elif color == "purple":
        if "red" not in colors_found or "blue" not in colors_found:
            colors_found.remove(color)
    elif color == "green":
        if "blue" not in colors_found or "yellow" not in colors_found:
            colors_found.remove(color)

print(colors_found)


"""                     Task:
You will have to find all possible color combinations that can be used.
Write a program that finds colors in a string. You will be given a string on a single
line containing substrings (separated by a single space) from which you will be able to
form the following colors:
Main colors: "red", "yellow", "blue"
Secondary colors: "orange", "purple", "green"
To form a color, you should concatenate the first and the last substrings and check if
you can get any of the above colors' names. If there is only one substring left,
you should use it to do the same check.
You can only keep a secondary color if the two main colors needed for its creation
could be formed from the given substrings:
•	orange = red + yellow
•	purple = red + blue
•	green = yellow + blue
Note: You could find some of the main colors needed to keep a secondary color after
it is found.
When you form a color, remove both substrings. Otherwise, you should remove the last
character of each substring and return them in the middle of the original string.
If the string contains an odd number of substrings, you should put the substrings one
position ahead.
For example, if you are given the string "re yellow bye" you could not form a color
with the substring "re" and "bye", so you should remove the last character and return
them in the middle of the string: "r by yellow".
In the end, print out the list with colors in the order in which they are found.
Input
•	Single line string
Output
•	The list with the collected colors
Constrains
•	You will not receive an empty string
•	Please consider only the colors mentioned above
•	There won't be any cases with repeating colors

Example:
Input:
r ue nge ora bl ed
Output:
['red', 'blue']

Example:
Input:
re ple blu pop e pur d
Output:
['red', 'purple', 'blue']
"""
