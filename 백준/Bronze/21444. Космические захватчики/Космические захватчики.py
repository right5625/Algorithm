from math import ceil

n, p = map(int, input().split())
print((n * 2 - p - 1 if ceil(n / 2) < p else n + p - 2) + sum(list(map(int, input().split()))))