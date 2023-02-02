# Write a function that receives two characters and returns a single string with all the characters in
# between them (according to the ASCII code), separated by a single space. Print the result on the console.

def numbers_between(start_number: str, end_number: str) -> list:
    result = []
    for number in range(ord(start_number) + 1, ord(end_number)):
        result.append(chr(number))
    return result


first_number = input()
second_number = input()
result_list = numbers_between(first_number, second_number)
# print(*result_list, sep=' ')
print(' '.join(result_list))
