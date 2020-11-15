from utils import fib_seq

c = 1
for i in fib_seq():
    c += 1
    if len(str(i)) >= 1000:
        print(c)
        break
