# Using a dictionary comprehension, write a program that receives country names on the first line,
# separated by comma and space ", ", and their corresponding capital cities on the second line
# (again separated by comma and space ", "). Print each country with their capital on a separate line in
# the following format: "{country} -> {capital}".
# Hints
# •	You could use the zip() method.

country_list = input().split(', ')
capitals_list = input().split(', ')
country_capital_dictionary = dict(zip(country_list, capitals_list))

for country, capital in country_capital_dictionary.items():
    print(f"{country} -> {capital}")
