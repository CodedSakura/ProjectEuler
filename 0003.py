from utils import primes

v = 600851475143
lim = v ** .5
last = 1
for i in primes():
    if v % i == 0:
        last = i
    if i > lim:
        break

print(last)
