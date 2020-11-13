from utils import primes

s = 0
for i in primes():
    if i > 2000000:
        break
    s += i

print(s)