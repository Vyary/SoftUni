t_shirt_price = float(input())
target_price = float(input())

shorts = t_shirt_price * 0.75
socks = shorts * 0.20
soccer_shoes = (shorts + t_shirt_price) * 2

total_price = t_shirt_price + shorts + socks + soccer_shoes
total_price *= 0.85

ball_won = False

if total_price >= target_price:
    ball_won = True

if ball_won:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_price:.2f} lv.")
else:
    diff = abs(target_price - total_price)
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")
