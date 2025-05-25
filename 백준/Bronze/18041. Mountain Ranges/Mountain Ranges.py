N, X = map(int, input().split())
A = list(map(int, input().split()))
result = 1
for i in range(N - 1):
    cnt, cur = 1, A[i]
    for j in range(i + 1, N):
        if A[j] - cur > X:
            break
        cnt += 1
        cur = A[j]
    result = max(result, cnt)
print(result)