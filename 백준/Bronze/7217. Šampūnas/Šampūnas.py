import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
lst = [False] * (N + 1)
lst[1] = True
for _ in range(K):
    lst[int(input())] = True
for i in range(2, N + 1):
    if not lst[i - 1]:
        lst[i] = True
print(lst.count(True))