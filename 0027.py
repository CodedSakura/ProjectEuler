from utils import is_prime


def consecutive_primes(_a, _b):
    n = 0
    while is_prime(n ** 2 + _a * n + _b):
        n += 1
    return n


max_con = (0, 0)
for a in range(-999, 1000):
    for b in range(2, 1001):
        v = consecutive_primes(a, b)
        if v > max_con[0]:
            max_con = (v, a*b)
print(max_con[1])
