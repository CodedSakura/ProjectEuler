from utils import divisors


def d(n):
    a = sum(divisors(n)) - n
    b = sum(divisors(a)) - a
    return a != b and b == n, (a, b) if b > a else (b, a)


pairs = []
for i in range(1, 10000):
    c, p = d(i)
    if c and p not in pairs:
        pairs.append(p)

print(sum([sum(i) for i in pairs]))
