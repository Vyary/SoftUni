contribution = input()
total_money = 0

while contribution != 'NoMoreMoney':
    contribution = float(contribution)
    if contribution < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {contribution:.2f}")
    total_money += contribution
    contribution = input()

print(f'Total: {total_money:.2f}')
