for a in range(2, 334):
    for b in range(a, 668-a):
        c = 1000 - a - b
        if b > c:
            continue

        if a ** 2 + b ** 2 == c ** 2:
            print(a*b*c);