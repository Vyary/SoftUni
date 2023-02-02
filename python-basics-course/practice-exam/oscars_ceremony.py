rent = int(input())

figurine = rent * 0.7
catering = figurine * 0.85
sound_system = catering * 0.5

total = rent + figurine + catering + sound_system

print(f'{total:.2f}')
