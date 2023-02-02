# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half.
# Then the cards in the two halves are perfectly interleaved, such that the original bottom card is still on
# the bottom and the original
# top card is still on top.
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once,
# gives ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space) and on the second line receives a count of
# faro shuffles that should be made. Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number.

card_deck = input().split(' ')
shuffle_times = int(input())
deck_middle = len(card_deck) // 2

for shuffles in range(shuffle_times):
    shuffled_deck = []
    right_deck = card_deck[:deck_middle]
    left_deck = card_deck[deck_middle:]
    for card in range(deck_middle):
        shuffled_deck.append(right_deck[card])
        shuffled_deck.append(left_deck[card])
    card_deck = shuffled_deck

print(card_deck)
