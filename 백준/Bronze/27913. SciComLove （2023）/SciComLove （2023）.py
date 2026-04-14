import sys
input = lambda: sys.stdin.readline().rstrip()

N, Q = map(int, input().split())
S = list('SciComLove' * (N // 10) + 'SciComLove'[:N % 10])
result = sum(1 if i.isupper() else 0 for i in S)
for _ in range(Q):
    X = int(input())
    if S[X - 1].islower():
        S[X - 1] = S[X - 1].upper()
        result += 1
    else:
        S[X - 1] = S[X - 1].lower()
        result -= 1
    print(result)