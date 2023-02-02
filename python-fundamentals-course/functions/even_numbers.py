# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a list of only the even numbers. Use filter().

def even_checker(number: int) -> bool:
    if number % 2 == 0:
        return True
    return False


def str_to_int(number: str) -> int:
    return int(number)


numbers = map(str_to_int, input().split(' '))
result = filter(even_checker, numbers)
print(list(result))
