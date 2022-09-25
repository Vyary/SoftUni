change = float(input())
number_of_coins = 0
change = round(change * 100)

while change != 0:

    if (change // 200) >= 1:
        number_of_coins += change // 200
        change -= (change // 200) * 200
    elif (change // 100) >= 1:
        number_of_coins += change // 100
        change -= (change // 100) * 100
    elif (change // 50) >= 1:
        number_of_coins += change // 50
        change -= (change // 50) * 50
    elif (change // 20) >= 1:
        number_of_coins += change // 20
        change -= (change // 20) * 20
    elif (change // 10) >= 1:
        number_of_coins += change // 10
        change -= (change // 10) * 10
    elif (change // 5) >= 1:
        number_of_coins += change // 5
        change -= (change // 5) * 5
    elif (change // 2) >= 1:
        number_of_coins += change // 2
        change -= (change // 2) * 2
    elif (change // 1) >= 1:
        number_of_coins += change // 1
        change -= (change // 1) * 1

print(int(number_of_coins))
