from utils import is_prime, primes, rotate_left

encountered = set()
for p in primes():
    if p > 1000000:
        break
    rotations = list(map(int, rotate_left(str(p))))
    if all(map(is_prime, rotations)):
        encountered.update(rotations)
print(len(encountered))
