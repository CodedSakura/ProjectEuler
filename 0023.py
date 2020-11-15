from utils import divisors


def is_abundant(n):
    return sum(divisors(n)) > 2 * n


abd = []
for i in range(28124):
    if is_abundant(i):
        abd.append(i)

possible = set()
for i in abd:
    for j in abd:
        if i + j > 28123:
            break
        possible.add(i + j)

print(sum([i for i in range(28123) if i not in possible]))
