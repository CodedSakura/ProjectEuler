from utils import fib_seq

s = 0
for i in fib_seq():
    if i > 4000000:
        break
    if i % 2 == 0:
        s += i

print(s)
