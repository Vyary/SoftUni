number_of_titles = int(input())

hs_sales = 0
fortnite_sales = 0
overwatch_sales = 0
others_sales = 0

for titles in range(number_of_titles):
    title = input()
    if title == 'Hearthstone':
        hs_sales += 1
    elif title == 'Fornite':
        fortnite_sales += 1
    elif title == 'Overwatch':
        overwatch_sales += 1
    else:
        others_sales += 1

percent_hs = (hs_sales / number_of_titles) * 100
percent_fn = (fortnite_sales / number_of_titles) * 100
percent_ow = (overwatch_sales / number_of_titles) * 100
percent_oth = (others_sales / number_of_titles) * 100


print(f"Hearthstone - {percent_hs:.2f}%")
print(f"Fornite - {percent_fn:.2f}%")
print(f"Overwatch - {percent_ow:.2f}%")
print(f"Others - {percent_oth:.2f}%")
