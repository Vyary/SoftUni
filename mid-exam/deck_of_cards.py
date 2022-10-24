deck = input().split(', ')
number_of_commands = int(input())

for number in range(number_of_commands):
    initial_command = input().split(', ')
    command = initial_command[0]

    if command == 'Add':
        card_name = initial_command[1]
        if card_name not in deck:
            deck.append(card_name)
            print('Card successfully added')
        else:
            print('Card is already in the deck')
    elif command == 'Remove':
        card_name = initial_command[1]
        if card_name in deck:
            deck.remove(card_name)
            print('Card successfully removed')
        else:
            print('Card not found')
    elif command == 'Remove At':
        card_index = int(initial_command[1])
        if card_index in range(len(deck)):
            deck.pop(card_index)
            print('Card successfully removed')
        else:
            print('Index out of range')

    elif command == 'Insert':
        card_index = int(initial_command[1])
        card_name = initial_command[2]
        if card_index in range(len(deck)):
            if card_name not in deck:
                deck.insert(card_index, card_name)
                print('Card successfully added')
            else:
                print('Card is already added')
        else:
            print('Index out of range')

print(', '.join(deck))
