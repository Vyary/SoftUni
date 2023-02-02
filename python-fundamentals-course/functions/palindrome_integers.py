# A palindrome is a number that reads the same backward as forward, such as 323 or 1001.
# Write a function that receives a list of positive integers, separated by comma and space ", ".
# The function should check if each integer is a palindrome - True or False. Print the result.

def palindrome_checker(num: str) -> bool:
    reversed_num = num[::-1]
    if num == reversed_num:
        return True
    return False


numbers = map(palindrome_checker, input().split(', '))
list_of_booleans = list(numbers)
print(*list_of_booleans, sep='\n')
