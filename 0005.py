from utils import factors, product

facMap = {}
for i in range(2, 21):
    facList = list(factors(i))
    facMapNew = {j: facList.count(j) for j in set(facList)}
    for j in set(list(facMapNew.keys()) + facList):
        if j in facMap:
            if j in facMapNew:
                facMap[j] = max(facMapNew[j], facMap[j])
        else:
            facMap[j] = facMapNew[j]

print(product([i[0] ** i[1] for i in facMap.items()]))
