def collatz(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
    yield 1


maxLen = (0, 0)
for i in range(1, 1000000):
    cLen = len(list(collatz(i)))
    if cLen > maxLen[0]:
        maxLen = (cLen, i)
print(maxLen[1])
