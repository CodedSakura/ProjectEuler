from utils import factors, product

facs = {}
for i in range(2, 21):
    l = list(factors(i))
    k = {j: l.count(j) for j in set(l)}
    for j in set(list(k.keys()) + l):
        if j in facs:
            if j in k:
                facs[j] = max(k[j], facs[j])
        else:
            facs[j] = k[j]

print(product([i[0] ** i[1] for i in facs.items()]))