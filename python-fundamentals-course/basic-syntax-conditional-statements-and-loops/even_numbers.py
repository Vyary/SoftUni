# Write a program that receives a number n on the first line. On the following n lines,
# it receives different integer numbers. If the program receives an odd number,
# print "{num} is odd!" and end the program. Otherwise, if all numbers given are even,
# print "All numbers are even.".

number_of_lines = int(input())

for _ in range(number_of_lines):
    current_number = int(input())
    if not current_number % 2 == 0:
        print(f'{current_number} is odd!')
        break
else:
    print('All numbers are even.')
