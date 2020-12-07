c = 1
s = 1
for i in range(2, 1001, 2):
    for j in range(4):
        c += i
        s += c
print(s)
