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

def product(list):
    res = 1
    for i in list:
        res *= i
    return res