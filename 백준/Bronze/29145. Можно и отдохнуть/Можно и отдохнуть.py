import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
result = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    if k >= a and (k - a) % b == 0:
        result += c
print(result)