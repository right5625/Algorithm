import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = [int(input()) for _ in range(N)]
result = 0
for i in range(1, N + 1):
    if i in A:
        result += 1
print(result)