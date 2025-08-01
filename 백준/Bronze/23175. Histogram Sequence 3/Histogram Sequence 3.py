n = int(input())
a = list(map(int, input().split()))
idx = 0
result = []
while idx < n:
    result.append(a[idx])
    idx += a[idx]
print(*result)