from typing import List


def get_primes(list: List[int]):
    for number in list:
        if number <= 1:
            continue

        for i in range(2, number):
            if number % i == 0:
                break
        else:
            yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
