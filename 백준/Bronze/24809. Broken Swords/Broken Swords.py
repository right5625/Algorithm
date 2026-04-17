import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
tb = lr = 0
for _ in range(N):
    S = input()
    if S[0] == '0':
        tb += 1
    if S[1] == '0':
        tb += 1
    if S[2] == '0':
        lr += 1
    if S[3] == '0':
        lr += 1
swords = min(tb // 2, lr // 2)
print(swords, tb - swords * 2, lr - swords * 2)