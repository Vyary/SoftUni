budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())

video_card_price = video_cards * 250
processor_price = (video_card_price * 0.35) * processors
ram_memory_price = (video_card_price) * 0.10 * ram_memory

total_price = video_card_price + processor_price + ram_memory_price

if video_cards > processors:
    total_price = total_price * 0.85

difference = abs(budget - total_price)

if total_price <= budget:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
