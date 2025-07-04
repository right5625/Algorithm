from collections import deque

N, L = map(int, input().split())
A = list(map(int, input().split()))
deq = deque()
for i in range(N):
    while deq and deq[-1][1] > A[i]:
        deq.pop()
    deq.append((i, A[i]))
    if deq[0][0] <= i - L:
        deq.popleft()
    print(deq[0][1], end = ' ')