from math import ceil

for _ in range(int(input())):
    n, s = map(int, input().split())
    print(ceil(max(list(map(int, input().split()))) * s / 1000))