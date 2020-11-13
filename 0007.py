from utils import primes

c = 0
for i in primes():
    c += 1
    if c == 10001:
        print(i)
        break
