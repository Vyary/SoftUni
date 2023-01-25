rows = int(input())

matrix = [[int(num) for num in input().split(", ")] for _ in range(rows)]

primary_diagonal = [matrix[num][num] for num in range(rows)]
secondary_diagonal = [matrix[num][rows - num - 1] for num in range(rows)]

print(
    f"Primary diagonal: {', '.join(str(num) for num in primary_diagonal)}. Sum: {sum(primary_diagonal)}"
)
print(
    f"Secondary diagonal: {', '.join(str(num) for num in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}"
)


"""                     Task:
Using a nested list comprehension, write a program that reads rows of a square matrix
and its elements, separated by a comma and a space ", ". You should find the matrix's
diagonals, prints them and their sum in the format:
"Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".

Example:
Input:
3
1, 2, 3
4, 5, 6
7, 8, 9
Output:
Primary diagonal: 1, 5, 9. Sum: 15
Secondary diagonal: 3, 5, 7. Sum: 15
"""
