# DP
n = int(input())
A = list(map(int, input().split()))
L = [0] * n
R = [0] * n
L[0] = A[0]
R[n - 1] = A[n - 1]
for i in range(1, n):
    L[i] = max(A[i], L[i - 1] + A[i])
for i in range(n - 2, -1, -1):
    R[i] = max(A[i], R[i + 1] + A[i])
res = max(L)
for i in range(1, n - 1):
    res = max(res, L[i - 1] + R[i + 1])
print(res)