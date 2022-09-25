# Write a program that reads a floating-point number and:
# -	prints "zero" if the number is zero
# -	prints "positive" or "negative"
# -	adds "small" if the absolute value of the number is less than 1, and it is not 0, or "large" if it exceeds
# 1 000 000

number_to_test = float(input())

number_is = ''

if number_to_test == 0:
    number_is = 'zero'
elif number_to_test > 0:
    number_is = 'positive'
    if number_to_test < 1:
        number_is = 'small positive'
    elif number_to_test > 1000000:
        number_is = 'large positive'
elif number_to_test < 0:
    number_is = 'negative'
    if number_to_test > -1:
        number_is = 'small negative'
    elif number_to_test < -1000000:
        number_is = 'large negative'

print(number_is)
