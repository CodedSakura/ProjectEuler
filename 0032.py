# WIP
unique = set()
for i in range(500):
    for j in range(500):
        if (sorted("".join(map(str, [i, j, i*j])))) == list("123456789"):
            unique.add(i*j)

print(sum(unique))  # wrong??
