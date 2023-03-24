from itertools import permutations
from typing import List


def possible_permutations(sequence: List[int]):
    for element in list(permutations(sequence)):
        yield list(element)


[print(n) for n in possible_permutations([1, 2, 3])]
