number_of_lines = int(input())

odd_set = set()
even_set = set()

for row in range(1, number_of_lines + 1):
    ascii_sum = sum(ord(letter) for letter in input()) // row
    if ascii_sum % 2 == 0:
        even_set.add(ascii_sum)
    else:
        odd_set.add(ascii_sum)

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")


"""                     Task:
You will receive a number N. On the following N lines, you will be receiving names.
You should sum the ASCII values of each letter in the name and integer divide it by
the number of the current row (starting from 1). Save the result to a set of either
odd or even numbers, depending on if the resulting number is odd or even. After that,
sum the values of each set.
•	If the sums of the two sets are equal, print the union of the values,
separated by ", ".
•	If the sum of the odd numbers is bigger than the sum of the even numbers,
print the different values, separated by ", ".
•	If the sum of the even numbers is bigger than the sum of the odd numbers,
print the symmetric-different values, separated by ", ".
Note: On every operation, the starting set should be the odd set

Example:
Input:
4
Pesho
Stefan
Stamat
Gosho
Output:
304, 128, 206, 511
"""
