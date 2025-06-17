import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    N = int(input())
    print(1 if N ** 0.5 == int(N ** 0.5) else 0)