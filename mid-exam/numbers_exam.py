nums = [int(num) for num in input().split(' ')]

while True:
    initial_command = input()
    if initial_command == 'Finish':
        break

    split_command = initial_command.split(' ')
    command = split_command[0]
    value = int(split_command[1])

    if command == 'Add':
        nums.append(value)
    elif command == 'Remove':
        if value in nums:
            nums.remove(value)
    elif command == 'Replace':
        replacement = int(split_command[2])
        if value in nums:
            index = nums.index(value)
            nums[index] = replacement
    elif command == 'Collapse':
        nums_copy = nums.copy()
        for num in nums_copy:
            if value > num:
                nums.remove(num)

print(*nums, sep=' ')
