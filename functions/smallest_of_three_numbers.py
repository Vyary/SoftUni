def str_to_int(number):
    int_number = int(number)
    return int_number


numbers_list = map(str_to_int, [input(), input(), input()])
print(min(numbers_list))
