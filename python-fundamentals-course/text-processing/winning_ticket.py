# The lottery is exciting. However, checking a million tickets for winnings only by hand is not.
# So, you are given the task of creating a program that automatically checks if a ticket is a winner.
# You are given a collection of tickets separated by commas and spaces (one or many).
# You need to check each ticket to see if it has a winning combination of symbols:
# •	A valid ticket has exactly 20 characters.
# •	A winning ticket is a valid one, containing one of the symbols '@', '#', '$' or '^' uninterruptedly repeated at
# least 6 times in both halves of the tickets.
# •	In order to win a Jackpot, the ticket should contain the same winning symbol 10 times on both sides
# An example of a valid winning ticket:
# "Cash$$$$$$Ca$$$$$$sh"
# An example of a Jackpot winning valid ticket:
# "$$$$$$$$$$$$$$$$$$$$"
# Input
# The input will be read from the console. The input consists of a single line containing all tickets separated by
# commas and one or more white spaces in the format:
# •	"{ticket}, {ticket}, … {ticket}"
# Output
# Print the result for every ticket in the order of their appearance, each on a separate line in the format:
# •	If the ticket is invalid: "invalid ticket"
# •	If the ticket is valid, but it is not winning: "ticket "{ticket}" - no match"
# •	If the ticket is valid and winning, but not a Jackpot:
# "ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}"
# •	It the ticket hits the Jackpot:
# "ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!"

def counter(searched_symbol: str, string: str) -> int:
    count = 0
    streak = 0

    for char in string:
        if char == searched_symbol:
            count += 1
            if count > streak:
                streak = count
        else:
            if count > streak:
                streak = count
            count = 0

    return streak


def winning_counter(ticket: str) -> [int, str]:
    winning_symbols = ['$', '#', '@', '^']
    left_part = ticket[:10]
    right_part = ticket[10:]
    min_side = 0
    winning_symbol = ''
    for symbol in winning_symbols:
        left_count = counter(symbol, left_part)
        right_count = counter(symbol, right_part)
        symbol_count = min(left_count, right_count)

        if symbol_count > min_side:
            min_side = symbol_count
            winning_symbol = symbol

    return min_side, winning_symbol


def main():
    tickets = input().replace(' ', '').split(',')
    for ticket in tickets:
        if len(ticket) != 20:
            print('invalid ticket')
            continue

        min_side, winning_symbol = winning_counter(ticket)

        if min_side == 10:
            print(f'ticket "{ticket}" - {min_side}{winning_symbol} Jackpot!')
        elif min_side >= 6:
            print(f'ticket "{ticket}" - {min_side}{winning_symbol}')
        elif min_side < 6:
            print(f'ticket "{ticket}" - no match')


if __name__ == '__main__':
    main()
