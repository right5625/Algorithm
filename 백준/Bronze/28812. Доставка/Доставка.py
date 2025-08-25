n, C = map(int, input().split())
result = 10 ** 9
for _ in range(n):
    p, d, v = map(int, input().split())
    result = min(result, p + d + C * v)
print(result)