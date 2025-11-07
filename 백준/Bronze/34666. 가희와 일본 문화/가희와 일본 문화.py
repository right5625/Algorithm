import sys
input = lambda: sys.stdin.readline().rstrip()

score = [0, 100, 90]
for _ in range(int(input())):
    A = list(map(int, input().split()))
    print('YES' if A[0] <= 2 and A[3] >= 50 and ((A[1] * 3 < score[A[0]] and A[2] * 3 < score[A[0]]) or (A[1] <= 21 or A[2] <= 21)) else 'NO')