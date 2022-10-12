# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a sorted list of numbers in ascending order. Use sorted().

def str_to_int(number: str) -> int:
    return int(number)


numbers = map(str_to_int, input().split(' '))
print(sorted(numbers))
