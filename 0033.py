prod = 1
for i in range(11, 99):
    if i % 10 == 0:
        continue
    for j in range(i + 1, 100):
        if j % 10 == 0:
            continue
        diff = set(str(i)).intersection(set(str(j)))
        for d in diff:
            # print(d, f"{i} / {j} = {i/j}")
            _i, _j = map(int, (str(i).replace(d, "", 1), str(j).replace(d, "", 1)))
            if i/j == _i/_j:
                prod *= i / j
print(round(1/prod))
