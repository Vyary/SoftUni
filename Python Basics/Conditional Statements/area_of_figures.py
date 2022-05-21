from math import pi
figure = input()
result = 0

if figure == 'square':
    side = float(input())
    result = side * side
elif figure == 'rectangle':
    length = float(input())
    width = float(input())
    result = length * width
elif figure == 'circle':
    area = float(input())
    result = pi * area * area
elif figure == 'triangle':
    base = float(input())
    height = float(input())
    result = (base * height) / 2

print(f"{result:.3f}")