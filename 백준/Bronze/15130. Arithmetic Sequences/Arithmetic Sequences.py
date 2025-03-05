A = list(map(int, input().split()))
idx = [i for i in range(10) if A[i]]
if (A[idx[1]] - A[idx[0]]) % (idx[1] - idx[0]) != 0:
    print(-1)
else:
    d = (A[idx[1]] - A[idx[0]]) // (idx[1] - idx[0])
    for i in range(idx[0] - 1, -1, -1):
        A[i] = A[i + 1] - d
    for i in range(idx[0] + 1, 10):
        A[i] = A[i - 1] + d
    print(*A)