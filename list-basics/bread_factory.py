# As a young baker, you are baking the bread out of the bakery.
# You have initial energy 100 and initial coins 100. You will be given a string representing the working day events.
# Each event is separated with '|' (vertical bar): "event1|event2| … eventN"
# Each event contains an event name or an ingredient and a number, separated by a dash ("{event/ingredient}-{number}")
# •	If the event is "rest":
# o	You gain energy (the number in the second part). Note: your energy cannot exceed your initial energy (100).
# Print: "You gained {gained_energy} energy.".
# o	After that, print your current energy: "Current energy: {current_energy}.".
# •	If the event is "order":
# o	You've earned some coins (the number in the second part).
# o	Each time you get an order, your energy decreases by 30 points.
# 	If you have the energy to complete the order, print: "You earned {earned} coins.".
# 	Otherwise, skip the order and gain 50 energy points. Print: "You had to rest!".
# •	In any other case, you have an ingredient you should buy. The second part of the event contains the coins you
# should spend.
# o	If you have enough money, you should buy the ingredient and print:
# "You bought {ingredient}."
# o	Otherwise, print "Closed! Cannot afford {ingredient}." and your bakery rush is over.
# If you managed to handle all events throughout the day, print on the following 3 lines:
# "Day completed!"
# "Coins: {coins}"
# "Energy: {energy}"
# Input / Constraints
# You will receive a string representing the working day events, separated with '|' (vertical bar) in the format:
# "event1|event2| … eventN".
# Each event contains an event name or an ingredient and a number, separated by a dash in the format:
# "{event/ingredient}-{number}"
# Output
# Print the corresponding messages described above.

import re

event_list = re.split('[-|]', input())

energy = 100
coins = 100
bakery_is_open = True

for event_index in range(0, len(event_list), 2):
    event = event_list[event_index]
    event_value = int(event_list[event_index + 1])
    if event == 'rest':
        current_energy = energy
        energy += event_value
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event == 'order':
        if 30 <= energy:
            coins += event_value
            energy -= 30
            print(f"You earned {event_value} coins.")
        else:
            print("You had to rest!")
            energy += 50
    else:  # ingredient to buy
        if coins - event_value >= 0:
            print(f"You bought {event}.")
            coins -= event_value
        else:
            print(f"Closed! Cannot afford {event}.")
            bakery_is_open = False
            break

if bakery_is_open:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
