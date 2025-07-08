def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

n = int(input())
for i in range(n // 2 - (1 - n % 2), 0, -1):
    if gcd(i, n - i) == 1:
        print(i, n - i)
        break