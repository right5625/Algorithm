result = float('inf')
for _ in range(int(input())):
    A, B, C = map(int, input().split())
    if A + B + C >= 512:
        result = min(result, A + B + C)
print(result if result != float('inf') else -1)