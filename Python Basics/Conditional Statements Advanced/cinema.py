type_of_ticket = input()
rolls = int(input())
columns = int(input())

price = 0
if type_of_ticket == 'Premiere':
    price = 12
elif type_of_ticket == 'Normal':
    price = 7.50
elif type_of_ticket == 'Discount':
    price = 5.00

total_price = price * rolls * columns

print(f'{total_price:.2f}')
