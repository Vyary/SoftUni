# Write a function that receives three integer numbers and returns the smallest. Print the result on the console.
# Use an appropriate name for the function.

def str_to_int(number: str) -> int:
    int_number = int(number)
    return int_number


numbers_list = map(str_to_int, [input(), input(), input()])
print(min(numbers_list))
