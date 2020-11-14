from utils import divisors


def triangle_number(n):
    return n * (n + 1) // 2


i = 1
while True:
    v = triangle_number(i)
    if len(list(divisors(v))) > 500:
        print(v)
        break
    if i % 100 == 0:
        print(f"[{i}; {v}]")
    i += 1
