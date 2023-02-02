text = input()
result = 0

for letter in text:
    if letter == 'a':
        result += 1
    elif letter == 'e':
        result += 2
    elif letter == 'i':
        result += 3
    elif letter == 'o':
        result += 4
    elif letter == 'u':
        result += 5

print(result)
