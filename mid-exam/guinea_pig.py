# Merry has a guinea pig named Puppy, that she loves very much. Every month she goes to the nearest pet store and
# buys him everything he needs – food, hay, and cover.
# On the first three lines, you will receive the quantity of food, hay, and cover, which Merry buys for
#     a month (30 days). On the fourth line, you will receive the guinea pig's weight.
# Every day Puppy eats 300 gr of food. Every second day Merry first feeds the pet, then gives it a certain amount of
# hay equal to 5% of the rest of the food. On every third day, Merry puts Puppy cover with
#     a quantity of 1/3 of its weight.
# Calculate whether the quantity of food, hay, and cover, will be enough for a month.
# If Merry runs out of food, hay, or cover, stop the program!
# Input
# •	On the first line – quantity food in kilograms - a floating-point number in the range [0.0 – 10000.0]
# •	On the second line – quantity hay in kilograms - a floating-point number in the range [0.0 – 10000.0]
# •	On the third line – quantity cover in kilograms - a floating-point number in the range [0.0 – 10000.0]
# •	On the fourth line – guinea's weight in kilograms - a floating-point number in the range [0.0 – 10000.0]
# Output
# •	If the food, the hay, and the cover are enough, print:
# o	"Everything is fine! Puppy is happy! Food: {excessFood}, Hay: {excessHay}, Cover: {excessCover}."
# •	If one of the things is not enough, print:
# o	"Merry must go to the pet store!"
# The output values must be formatted to the second decimal place!

quantity_food = float(input()) * 1000
quantity_hay = float(input()) * 1000
quantity_cover = float(input()) * 1000
guineas_weight = float(input()) * 1000
food_is_not_enough = False

for day in range(1, 30 + 1):
    quantity_food -= 300
    if day % 2 == 0:
        quantity_hay -= quantity_food * 0.05
    if day % 3 == 0:
        quantity_cover -= guineas_weight / 3

    if quantity_food <= 0 or quantity_hay <= 0 or quantity_cover <= 0:
        food_is_not_enough = True
        break

food_left = quantity_food / 1000
hay_left = quantity_hay / 1000
cover_left = quantity_cover / 1000

if food_is_not_enough:
    print('Merry must go to the pet store!')
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_left:.2f}, Hay: {hay_left:.2f}, Cover: {cover_left:.2f}.")
