from math import ceil

N, K = map(int, input().split())
print(*[1 if i <= ceil(N / 2) else N for i in list(map(int, input().split()))])