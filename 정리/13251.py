# 조합
M = int(input())
lst = list(map(int, input().split()))
K = int(input())
N = sum(lst)
res = 0
for i in range(M):
    t = 1
    for j in range(K):
        t *= (lst[i] - j) / (N - j)
    res += t
print(res)