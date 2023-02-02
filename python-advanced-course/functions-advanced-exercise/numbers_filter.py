def even(*args):
    return [x for x in args if x % 2 == 0]


def odd(*args):
    return [x for x in args if x % 2 == 1]


def even_odd_filter(**kwargs):
    numbers = {}

    for key, values in kwargs.items():
        if key == "odd":
            numbers[key] = list(filter(odd, values))
        elif key == "even":
            numbers[key] = list(filter(even, values))

    return dict(sorted(numbers.items(), key=lambda x: -len(x[1])))


"""                     Task:
Create a function called even_odd_filter() that can receive a different number of
named arguments. The keys will be "even" and/or "odd",
and the values will be a list of numbers.
When the key is "odd", you should extract only the odd numbers from its list.
When the key is "even", you should extract only the even numbers from its list.
The function should return a dictionary sorted by the length of the lists in
descending order. There will be no case of lists with the same length.

Example:
Test Code:
print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
Output:
{'even': [4, 10, 2, 2], 'odd': [1, 3, 5]}
"""
