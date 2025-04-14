N, M = map(int, input().split())
T = list(map(int, input().split()))
dic = {i: 0 for i in range(1, N + 1)}
for i in range(N):
    S = list(map(int, input().split()))
    for j in range(M):
        if S[j] == T[j]:
            dic[i + 1] += 1
print(sorted(dic.items(), key=lambda x: (-x[1], x[0]))[0][0])