number_1 = int(input())
number_2 = int(input())
operator = input()

result = 0
if operator == '+':
    result = number_1 + number_2
elif operator == '-':
    result = number_1 - number_2
elif operator == '*':
    result = number_1 * number_2
elif operator == '/':
    if number_1 != 0 and number_2 != 0:
        result = number_1 / number_2
elif operator == '%':
    if number_1 != 0 and number_2 != 0:
        result = number_1 % number_2

even_or_odd = ''
if result % 2 == 0:
    even_or_odd = 'even'
else:
    even_or_odd = 'odd'

difference = abs(number_1 - number_2)

if operator == '+' or operator == '-' or operator == '*':
    print(f"{number_1} {operator} {number_2} = {result} - {even_or_odd}")
elif operator == '/':
    if number_1 != 0 and number_2 != 0:
        print(f'{number_1} / {number_2} = {result:.2f}')
    else:
        print(f"Cannot divide {difference} by zero")
elif operator == '%':
    if number_1 != 0 and number_2 != 0:
        print(f"{number_1} % {number_2} = {result}")
    else:
        print(f"Cannot divide {difference} by zero")
