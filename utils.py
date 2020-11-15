def primes():
    def next_prime(prev=2):
        if prev % 2 == 0:
            curr = prev + 1
        else:
            curr = prev + 2

        for i in range(3, int(curr ** .5 + 1), 2):
            if curr % i == 0:
                return next_prime(curr)
        return curr
    
    a = 2
    while True:
        yield a
        a = next_prime(a)


def fib_seq():
    a = 1
    b = 1
    while True:
        yield b
        t = a
        a = b
        b += t


def factors(n):
    c = 2
    while n > 1:
        while n % c == 0:
            yield c
            n /= c
        c += 1


def product(values):
    res = 1
    for i in values:
        res *= i
    return res


def divisors(n):
    for i in range(1, int(n ** .5 + 1)):
        if n % i == 0:
            if n // i == i:
                yield i
            else:
                yield i
                yield n // i


def factorial(n):
    c = 1
    for i in range(1, n+1):
        c *= i
    return c


def pascals_triangle(row, col):
    return factorial(row) // (factorial(col) * factorial(row - col))


def permutations(values):
    # for i in range(len(values)):
    #     v = values[i]
    #     subs = values[:i] + values[i+1:]
    #     print(i, v, subs, values)
    #     for j in permutations(subs):
    #         yield [v] + j
    r = list(range(len(values)-1))
    while True:
        yield list(values)
        k = -1
        for i in r:
            if values[i] < values[i+1]:
                k = i

        if k == -1:
            break

        l = -1
        for i in range(k, len(values)):
            if values[i] > values[k] and i > l:
                l = i

        (values[k], values[l]) = (values[l], values[k])
        values = values[:k+1] + values[:k:-1]

