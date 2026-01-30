import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    N, M = map(int, input().split())
    print(N + M - 1)