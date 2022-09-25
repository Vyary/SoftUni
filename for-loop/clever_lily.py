age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
money = 0
money_inc = 10

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        money += money_inc
        money_inc += 10
        money -= 1
    else:
        money += toy_price

diff = abs(money - washing_machine_price)
if money >= washing_machine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
