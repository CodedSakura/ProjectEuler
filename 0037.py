from utils import primes, is_prime

c = 0
s = 0
for p in primes():
    if p < 10:
        continue
    if c >= 11:
        break
    truncations = set([int(str(p)[:i]) for i in range(1, len(str(p)))] +
                      [int(str(p)[i:]) for i in range(1, len(str(p)))])
    if all(map(is_prime, truncations)):
        c += 1
        s += p
print(s)
