def cache(func):
    log = {}

    def wrapper(n):
        if n not in wrapper.log:
            wrapper.log[n] = func(n)
        return wrapper.log[n]

    wrapper.log = log
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(3)
print(fibonacci.log)  # {0: 0, 1: 1, 2: 1, 3: 2}

fibonacci(4)
print(fibonacci.log)  # {0: 0, 1: 1, 2: 1, 3: 2, 4: 3}
