from utils import is_palindrome

s = 0
for i in range(1000000):
    if is_palindrome(str(i)) and is_palindrome(f"{i:b}"):
        print(i, f"{i:b}")
        s += i
print(s)
