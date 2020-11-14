date = [1901, 1, 1]
months31 = [1, 3, 5, 7, 8, 10, 12]
weekday = 1


def is_leap(x):
    return x % 4 == 0 and x % 400 != 0


c = 0
while date[0] < 2001:
    if date[2] == 1 and weekday % 7 == 6:
        c += 1

    date[2] += 1
    weekday += 1

    if date[1] == 2 and (date[2] > (29 if is_leap(date[0]) else 28)):
        date[1] += 1
        date[2] = 1
    elif date[1] in months31 and date[2] > 31:
        date[1] += 1
        date[2] = 1
    elif date[1] not in months31 and date[2] > 30:
        date[1] += 1
        date[2] = 1

    if date[1] > 12:
        date[0] += 1
        date[1] = 1

print(c)
