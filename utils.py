# <editor-fold desc="Sequences">
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


def pascals_triangle(row, col):
    return factorial(row) // (factorial(col) * factorial(row - col))


def long_division(divisor, dividend=1, trim_leading=False):
    if trim_leading:
        while dividend < divisor:
            dividend *= 10
    while True:
        quotient = dividend // divisor
        yield quotient
        dividend -= quotient * divisor  # subtract reminder
        dividend *= 10
# </editor-fold>


# <editor-fold desc="Checks">
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** .5 + 1)):
        if n % i == 0:
            return False
    return True


def is_palindrome(text):
    if text == "":
        return None
    if len(text) == 1:
        return True
    if len(text) % 2 == 1:
        return text[:len(text)//2+1] == text[len(text)//2:][::-1]
    return text[:len(text)//2] == text[len(text)//2:][::-1]
# </editor-fold>


# <editor-fold desc="Operations">
def product(values):
    res = 1
    for i in values:
        res *= i
    return res


def factorial(n):
    c = 1
    for i in range(1, n+1):
        c *= i
    return c


def digits(num):
    return list(map(int, str(num)))


def rotate_left(l):
    for i in range(len(l)):
        yield l[i:] + l[:i]
# </editor-fold>


# <editor-fold desc="Maths">
def factors(n):
    c = 2
    while n > 1:
        while n % c == 0:
            yield c
            n /= c
        c += 1


def divisors(n):
    for i in range(1, int(n ** .5 + 1)):
        if n % i == 0:
            if n // i == i:
                yield i
            else:
                yield i
                yield n // i


def permutations(values):
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
# </editor-fold>


# <editor-fold desc="Extras">
def xrange(n):
    a = 0
    while a < n:
        yield a
        a += 1


def slice_generator(gen, n):
    return [next(gen) for _ in xrange(n)]
# </editor-fold>
