from collections import deque

N, K = map(int, input().split())
A = deque(map(int, input().split()))
R = deque([False] * N)
cnt = res = 0
while cnt < K:
    A.appendleft(A.pop())
    R.pop()
    R.appendleft(False)
    R[N - 1] = False
    for i in range(N - 1, 0, -1):
        if A[i] and R[i - 1] and not R[i]:
            R[i] = True
            R[i - 1] = False
            A[i] -= 1
            if A[i] == 0:
                cnt += 1
    if A[0] and not R[0]:
        A[0] -= 1
        R[0] = True
        if A[0] == 0:
            cnt += 1
    res += 1
print(res)