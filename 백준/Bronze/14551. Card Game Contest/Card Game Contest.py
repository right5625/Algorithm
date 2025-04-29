N, M = map(int, input().split())
result = 1
for _ in range(N):
    A = int(input())
    if A > 0:
        result *= A
print(result % M)