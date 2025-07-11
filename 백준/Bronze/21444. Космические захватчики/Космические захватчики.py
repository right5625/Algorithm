from math import ceil

n, p = map(int, input().split())
a = list(map(int, input().split()))
if ceil(n / 2) < p:
    print(n - p + n - 1 + sum(a))
else:
    print(p - 1 + n - 1 + sum(a))