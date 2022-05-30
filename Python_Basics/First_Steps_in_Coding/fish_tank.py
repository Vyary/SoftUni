length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = (length * width * height) * 0.001
water_needed = volume - volume * (percent / 100)

print(water_needed)
