# Write a program that receives a number and creates the following pattern.
# The number represents the largest count of stars on one row.

# *
# **
# ***
# **
# *

number = int(input())

for star in range(number):
    print(star * '*')

for star in range(number, -1, -1):
    print(star * '*')
