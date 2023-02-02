occurrences = {}

for letter in input():
    if letter not in occurrences:
        occurrences[letter] = 0
    occurrences[letter] += 1

for letter, occurrences in sorted(occurrences.items()):
    print(f"{letter}: {occurrences} time/s")


"""                     Task:
Write a program that reads a text from the console and counts the occurrences of each
character in it. Print the results in alphabetical (lexicographical) order.

Example:
Input:
Why do you like Python?
Output:
 : 4 time/s
?: 1 time/s
P: 1 time/s
W: 1 time/s
d: 1 time/s
e: 1 time/s
h: 2 time/s
i: 1 time/s
k: 1 time/s
l: 1 time/s
n: 1 time/s
o: 3 time/s
t: 1 time/s
u: 1 time/s
y: 3 time/s
"""
