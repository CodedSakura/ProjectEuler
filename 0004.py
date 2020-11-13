def is_palindrome(num):
    num = str(num)
    return num == num[::-1]

done = False
for i in range(999, 900, -1):
    for j in range(999, 900, -1):
        if is_palindrome(i*j):
            print(i*j)
            done = True
            break
    if done:
        break
