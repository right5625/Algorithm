N = int(input())
A = list(map(int, input().split()))
result = 0
for i in range(1, N + 1):
    idx1 = A.index(i)
    idx2 = A.index(i, idx1 + 1)
    result = max(result, idx2 - idx1 - 1)
print(result)