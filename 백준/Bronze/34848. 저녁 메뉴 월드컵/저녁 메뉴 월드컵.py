import sys, math
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    N = int(input())
    result = 0
    while N > 1:
        result += N % 2
        N = math.ceil(N / 2)
    print(result)