from utils import slice_generator, long_division


def find_pattern(v):
    for lam in range(30):
        for n in range(5, 2000):
            if v[lam:lam+n] == v[lam+n:lam+2*n]:
                return n


max_pat = (0, 0)
for i in range(2, 1000):
    l = find_pattern(slice_generator(long_division(i, trim_leading=True), 4100))
    if l > max_pat[0]:
        max_pat = (l, i)

print("\n", max_pat[1])
