import sys
input = lambda: sys.stdin.readline().rstrip()

N, C = map(int, input().split())
A = B = N
for _ in range(C):
    X, Y = map(int, input().split())
    if X < A and Y < B:
        if X * B >= Y * A:
            A = X
        else:
            B = Y
print(A * B)