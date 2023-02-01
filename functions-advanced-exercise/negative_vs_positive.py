numbers = list(map(int, input().split()))

positive_numbers = sum([num for num in numbers if num > 0])
negative_numbers = sum([num for num in numbers if num < 0])

print(negative_numbers)
print(positive_numbers)
if abs(negative_numbers) > positive_numbers:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")


"""                     Task:
You will receive a sequence of numbers (integers) separated by a single space.
Separate the negative numbers from the positive. Find the total sum of the negatives
and positives, and print the following:
•	On the first line, print the sum of the negatives
•	On the second line, print the sum of the positives
•	On the third line:
o	If the absolute negative number is larger than the positive number:
"The negatives are stronger than the positives"
o	If the positive number is larger than the absolute negative number:
"The positives are stronger than the negatives"
Note: you will not receive any zeroes in the input.

Example:
Input:
1 2 -3 -4 65 -98 12 57 -84
Output:
-189
137
The negatives are stronger than the positives
"""
