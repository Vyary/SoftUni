processor_price = float(input())
video_card_price = float(input())
ram_memory_price = float(input())
number_of_ram_modules = int(input())
discount = float(input())

usd_to_bgn = 1.57

processor_price_bgn = processor_price * usd_to_bgn * (1 - discount)
video_card_price_bgn = video_card_price * usd_to_bgn * (1 - discount)
ram_memory_price_bgn = (ram_memory_price * usd_to_bgn) * number_of_ram_modules

total = processor_price_bgn + video_card_price_bgn + ram_memory_price_bgn

print(f"Money needed - {total:.2f} leva.")
