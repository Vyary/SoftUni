number = input()
primer_total = 0
non_prime_total = 0

while number != 'stop':
    number = int(number)
    if number < 0:
        print("Number is negative.")
        number = 0
    count = 0
    for index in range(1, number + 1):
        if number % index == 0:
            count += 1

    if count == 2:
        primer_total += number
    elif count > 2:
        non_prime_total += number

    number = input()

print(f"Sum of all prime numbers is: {primer_total}")
print(f"Sum of all non prime numbers is: {non_prime_total}")
