# Write a program that helps you keep track of your shot targets. You will receive a sequence with integers,
#     separated by a single space, representing targets and their value. Afterward, you will be receiving indices until
#     the "End" command is given, and you need to print the targets and the count of shot targets.
# Every time you receive an index, you need to shoot the target on that index, if it is possible.
# Every time you shoot a target, its value becomes -1, and it is considered shot. Along with that, you also need to:
# •	Reduce all the other targets, which have greater values than your current target, with its value.
# •	Increase all the other targets, which have less than or equal value to the shot target, with its value.
# Keep in mind that you can't shoot a target, which is already shot. You also can't increase or reduce a target,
# which is considered shot.
# When you receive the "End" command, print the targets in their current state and the count of shot targets in
# the following format:
# "Shot targets: {count} -> {target1} {target2}… {targetn}"
# Input / Constraints
# •	On the first line of input, you will receive a sequence of integers,
# separated by a single space – the targets sequence.
# •	On the following lines, until the "End" command,
# you be receiving integers each on a single line – the index of the target to be shot.

targets = [int(num) for num in input().split(' ')]
count_of_shot_targets = 0

while True:
    command = input()
    if command == "End":
        break

    shot_index = int(command)
    if shot_index in range(len(targets)):
        if targets[shot_index] == -1:
            continue
        count_of_shot_targets += 1
        target_number = targets[shot_index]
        for index, num in enumerate(targets):
            if num > target_number and num != -1:
                num -= target_number
                targets[index] = num
            elif num <= target_number and num != -1:
                num += target_number
                targets[index] = num
        targets[shot_index] = -1

print(f"Shot targets: {count_of_shot_targets} ->", end=' ')
print(*targets, sep=' ')
