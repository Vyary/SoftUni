number_of_lines = int(input())

longest_intersection = []

for _ in range(number_of_lines):
    first_data, second_data = input().split("-")

    first_start, first_end = first_data.split(",")
    first_range = set(range(int(first_start), int(first_end) + 1))

    second_start, second_end = second_data.split(",")
    second_range = set(range(int(second_start), int(second_end) + 1))

    common = first_range.intersection(second_range)

    if len(common) > len(longest_intersection):
        longest_intersection = list(common)

print(
    f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}"
)


"""                     Task:
Write a program that finds the longest intersection.
You will be given a number N. On each of the next N lines you will be given two ranges
in the format: "{first_start},{first_end}-{second_start},{second_end}".
You should find the intersection of these two ranges. The start and end numbers in
the ranges are inclusive.
Finally, you should find the longest intersection of all N intersections,
print the numbers that are included and its length in the format: "Longest intersection
is [{longest_intersection_numbers}] with length {length_longest_intersection}"
Note: in each range, there will always be an intersection.
If there are two equal intersections, print the first one.

Example:
Input:
3
0,3-1,2
2,10-3,5
6,15-3,10
Output:
Longest intersection is [6, 7, 8, 9, 10] with length 5
"""
