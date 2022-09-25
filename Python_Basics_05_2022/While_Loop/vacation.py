trip_cost = float(input())
available_money = float(input())

total_days = 0
spend_count = 0
too_much_spending = False

while available_money < trip_cost:
    action = input()
    amount = float(input())
    total_days += 1

    if action == 'spend':
        available_money -= amount
        if available_money < 0:
            available_money = 0
        spend_count += 1
        if spend_count >= 5:
            too_much_spending = True
            break
    elif action == "save":
        available_money += amount
        spend_count = 0

if too_much_spending:
    print(f"You can't save the money.")
    print(f"{total_days}")
else:
    print(f"You saved the money for {total_days} days.")
