# It's the end of the week, and it is time for you to go shopping, so you need to create a shopping list first.
# Input
# You will receive an initial list with groceries separated by an exclamation mark "!".
# After that, you will be receiving 4 types of commands until you receive "Go Shopping!".
# •	"Urgent {item}" - add the item at the start of the list.  If the item already exists, skip this command.
# •	"Unnecessary {item}" - remove the item with the given name, only if it exists in the list.
# Otherwise, skip this command.
# •	"Correct {oldItem} {newItem}" - if the item with the given old name exists, change its name with the new one.
# Otherwise, skip this command.
# •	"Rearrange {item}" - if the grocery exists in the list, remove it from its current position and
# add it at the end of the list. Otherwise, skip this command.
# Constraints
# •	There won't be any duplicate items in the initial list
# Output
# •	Print the list with all the groceries, joined by ", ":
# "{firstGrocery}, {secondGrocery}, … {nthGrocery}"

shopping_list = input().split('!')

while True:
    command = input()
    if command == 'Go Shopping!':
        break

    split_command = command.split()
    if split_command[0] == 'Urgent':
        if split_command[1] not in shopping_list:
            shopping_list.insert(0, split_command[1])
    elif split_command[0] == 'Unnecessary':
        if split_command[1] in shopping_list:
            shopping_list.remove(split_command[1])
    elif split_command[0] == 'Correct':
        if split_command[1] in shopping_list:
            element_index = shopping_list.index(split_command[1])
            shopping_list[element_index] = split_command[2]
    elif split_command[0] == 'Rearrange':
        if split_command[1] in shopping_list:
            shopping_list.remove(split_command[1])
            shopping_list.append(split_command[1])

print(*shopping_list, sep=', ')
