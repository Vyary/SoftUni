total_steps = 0

while total_steps < 10000:
    action = input()
    if action == 'Going home':
        last_action = int(input())
        total_steps += last_action
        break
    total_steps += int(action)

diff = abs(total_steps - 10000)
if total_steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
