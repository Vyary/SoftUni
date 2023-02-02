# A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
# That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
# Write a function that receives an integer number and returns one of the following messages:
# •	"We have a perfect number!" - if the number is perfect.
# •	"It's not so perfect." - if the number is NOT perfect.
# Print the result on the console.

def perfect_number(num: int) -> bool:
    num_sum = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            num_sum += divisor
    if num_sum == num:
        return True
    return False


number = int(input())
is_perfect_number = perfect_number(number)
if is_perfect_number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
