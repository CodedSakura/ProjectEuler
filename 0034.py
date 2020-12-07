from utils import factorial, digits

s = 0
for i in range(3, 1000000):
    if sum(map(factorial, digits(i))) == i:
        s += i
print(s)
