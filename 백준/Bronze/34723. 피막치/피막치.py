P, M, C = map(int, input().split())
X = int(input())
result = float('inf')
for p in range(1, P + 1):
    for m in range(1, M + 1):
        for c in range(1, C + 1):
            result = min(result, abs((p + m) * (m + c) - X))
print(result)