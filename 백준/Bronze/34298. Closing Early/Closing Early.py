R, S, N = map(int, input().split())
A = list(map(int, input().split()))
if R == 0:
    print(0)
else:
    cur, result = 0, -1
    for i in range(N):
        cur += A[i]
        if cur % S == R:
            result = i + 1
            break
    print(result)