# Using a list comprehension, write a program that receives numbers, separated by comma and space ", ", and
# prints all the positive, negative, even, and odd numbers on separate lines as shown below.
# Note: Zero is counted for a positive number

num_lst = [int(num) for num in input().split(', ')]

positive_numbers = [str(num) for num in num_lst if num >= 0]
negative_numbers = [str(num) for num in num_lst if num < 0]
even_numbers = [str(num) for num in num_lst if num % 2 == 0]
odd_numbers = [str(num) for num in num_lst if num % 2 != 0]

print(f'''Positive: {", ".join(positive_numbers)}
Negative: {", ".join(negative_numbers)}
Even: {", ".join(even_numbers)}
Odd: {", ".join(odd_numbers)}
''')
