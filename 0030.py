from utils import digits

s = 0
for i in range(2, 1000000):
    if sum([i ** 5 for i in digits(i)]) == i:
        s += i

print(s)  # 443840
